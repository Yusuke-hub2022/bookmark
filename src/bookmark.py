import sys, pathlib, re, string, pprint

class Bookmark:
    def __init__(self):
        self.source = SourceData()
        self.pageData = PageData()
        self.html = Html()
        self.css = Css()

    def make(self, sourcePath, dest):
        lines = self.source.get(sourcePath)
        pageData = self.pageData.get(lines)
        html = self.html.generate(pageData)
        self.html.write(html, sourcePath, dest)
        self.css.setup(dest)

class SourceData:
    def get(self, sourcePath):
        with open(sourcePath, encoding='utf-8') as f:
            lines = f.readlines()
        cleaned = self.clean(lines)
        return cleaned
    
    def clean(self, lines):
        striped = [self.strip(l) for l in lines]
        proper = [l for l in striped if not self.is_ignore(l)]
        return proper

    def strip(self, line):
        withoutComment = re.sub(';;.*', '', line)
        striped = withoutComment.strip()
        return striped

    def is_ignore(self, line):
        if line.startswith('title:'):
            return False
        if re.match('>>>.+', line):
            return False
        if '---' in line:
            return False
        return True

class PageData:
    def get(self, lines):
        title = self.getTitle(lines[0])
        groups = self.getGroups(lines[1:]) # タイトルは除く

        return {
            'title': title,
            'groups': groups
        }
    
    def getTitle(self, text):
        title = 'Bookmark'
        if text.startswith('title:'):
            title = text.replace('title:','').strip()
        return title
    
    def getGroups(self, lines):
        separated = self.separateByGroup(lines)
        groups = []
        for groupChank in separated:
            groups.append(self.getGroupData(groupChank))
        return groups

    def separateByGroup(self, lines):
        groups = []
        group = []
        for l in lines:
            if l.startswith('>>>'):
                groups.append(group)
                group = []
                group.append(l)
                continue
            group.append(l)
        groups.append(group)

        if not groups[0]:  # 通常、先頭は空リスト（[]）
            groups = groups[1:] 
        return groups

    def getGroupData(self, groupChank):
        title = 'No Title'
        if groupChank[0].startswith('>>>'):
            title = groupChank[0].replace('>>>', '').strip()
            groupChank = groupChank[1:]

        return {
            'title': title,
            'links': groupChank
        }
        
class Html:
    def generate(self, pageData):
        pageTitle = pageData['title']
        groupsHtml = '\n'.join(self.groupsHtml(pageData['groups']))
        d = dict(title=pageTitle, groups=groupsHtml)
        s = string.Template(Template.page)
        html = s.safe_substitute(d)
        return html

    def groupsHtml(self, groups):
        html = []
        for g in groups:
            html.append('{}<div class="group">'.format(self.indent(2)))
            html.append('{}<h2>{}</h2>'.format(self.indent(3), g['title']))
            html.extend(self.groupHtml(g['links']))
            html.append('{}</div>'.format(self.indent(2)))
        return html

    def groupHtml(self, links):
        html = []
        html.append('{}<ul class="links">'.format(self.indent(3)))
        for l in links:
            html.append('{}<li>{}</li>'.format(self.indent(4), self.linkHtml(l)))
        html.append('{}</ul>'.format(self.indent(3)))
        return html
    
    def linkHtml(self, link):
        # link: 'title---url'
        title, url = link.split('---')
        html = '<a href="{}">{}</a>'.format(url, title)
        return html

    def indent(self, depth):
        return '  ' * depth

    def write(self, html, sourcePath, dest):
        htmlPath = sourcePath.with_suffix('.html')
        htmlPath = dest.joinpath(htmlPath.name)
        if not dest.exists():
            dest.mkdir(parents=True)
        with open(htmlPath, 'w', encoding='utf-8') as f:
            f.write(html)

class Template:
    page = '''<!doctype html>
<html>
<head>
<title>${title}</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="css/style.css" rel="stylesheet" type="text/css">
<link href="https://use.fontawesome.com/releases/v6.1.1/css/all.css" rel="stylesheet">
</head>
<body>
<div id="contents">
  <div id="head"><h1>${title}</h1></div>
  <div id="groups">

${groups}

  </div>
</div>
</body>
</html>'''

class Css:
    code = '''
* {
	margin: 0;
	padding:0;
}

body {
    background: rgb(202, 201, 194);
    color:rgb(129, 129, 129);
}

#contents {
	padding: 1em 1em;
}

h1 {
    color: rgb(105, 42, 105);
    font-weight: normal;
    margin: 0.25em 0em 0.5em 0em;
    font-size: 160%;
    letter-spacing: 0.16em;
}


h2 {
	padding: 0.5em;
    border-top: solid 2px #e000e0;
	background: #535;
    letter-spacing: 0.16em;
	font-size: medium;
	font-width: normal;
	font-weight: normal;
	color: #E1B8ED;
}

.group {
	padding-left: 1px;
	font-size: normal;
	letter-spacing: 0.05em;
}

li {
    position: relative; /* font awsome 用 */
	list-style-type: none;
    border-bottom: dotted 1px #767;
    line-height: 2em;
	color: #4c0e5f;
}

li::before {
    font-family: "Font Awesome 6 Free";
    font-weight: 900;
    content: '\\f138';
    position: absolute;
    left: 0.5em;
    top: 0.5em;
    /*color:#e000e0;*/
}

a {
    display: block;
    background: url("../img/linkmark.png") 1em 1em no-repeat;
    padding: 0.5em 1em 0.5em 2.25em;
    color:rgb(76, 0, 92);
	text-decoration: none;
    
}

a:hover {
    background-color: rgb(182, 180, 169);
    color:rgb(61, 61, 61)
}
    '''
    def setup(self, dest):
        cssDir = dest.joinpath('css')
        cssFile = dest.joinpath('css', 'style.css')
        if cssFile.exists():
            return
        if not cssDir.exists():
            cssDir.mkdir(parents=True)
        cssFile.write_text(self.code, encoding='utf-8')

    
Usage = '\nUsage: python bookmark.py source [destination]\n'

def main(args):
    if len(args) < 2:
        print(Usage)
        return
    sourcePath = pathlib.Path(args[1])
    dest = pathlib.Path(args[2]) if len(args) > 2 else sourcePath.parent # 無ければsourcePathと同じディレクトリ
    Bookmark().make(sourcePath, dest)

if __name__ == '__main__':
    main(sys.argv)