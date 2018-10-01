from lxml import etree


html = '''  
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF‐8" />
       <title>测试页面</title> 
   </head>
   <body> 
        <ol>
            <li class="haha">醉卧沙场君莫笑，古来征战几人回</li>
            <li class="heihei">两岸猿声啼不住，轻舟已过万重山</li>
            <li id="hehe" class="nene">一骑红尘妃子笑，无人知是荔枝来</li> 
            <li class="xixi">停车坐爱枫林晚，霜叶红于二月花</li>
            <li class="lala">商女不知亡国恨，隔江犹唱后庭花</li>       
        </ol>
       <div id="pp">
           <div>
               <a href="http://www.baidu.com">李白</a>
           </div> 
           <ol>
                <li class="huanghe">君不见黄河之水天上来，奔流到海不复回</li> 
                <li id="tata"  class="hehe">李白乘舟将欲行，忽闻岸上踏歌声</li>
                 <li class="tanshui">桃花潭水深千尺，不及汪伦送我情</li>
           </ol>
           <div class="hh">
                 <a href="http://mi.com">雷军</a> 
           </div>
           <ol>
                <li class="dudu">are you ok</li>
                <li class="meme">会飞的猪</li>
           </ol> 
        </div>
   </body>
   </html>
   '''

html_tree = etree.HTML(html)
#print(html_tree)
#获取所有的li节点
ret1 = html_tree.xpath('//li')
#获取所有li标签的class属性
ret2 = html_tree.xpath('//li/@class')
print(ret2)
#获取每一个ul标签的最后一个li标签的文本
# ret3 = html_tree.xpath('//li[last()]/text()')
# print(ret3)