//exo d'aplli sur DOM

<html>
<body>
  <div>Users:</div>
  <ul>
    <li>John</li>
    <li>Pete</li>
  </ul>
  <script>
    //Access the div
    //first way
    let div=document.bodychildren[0]
    //2nd way
    let div1=document.getElementByTagName('div')[0]
    //3rd way
    let div 2=document.querySlector('div')
    //4th way
    let div3=document.body.firstElementChild

    //access ul
    let ul=document.getElementByTagName('ul')[0]
    let ul2=document.body.children[1]
    let ul3=documentquerySelector('ul')
    let ul4=div.nextElementSibling

    //accessing the 2nd li
    letli=document.getElementByTagName('li')[1]
    let li1=ul.children[1]
    let ul2=ul.lastchild 
    //changer pete en paul
    console.log(innerHTML)//ceci nous donne la donnee avant le changement
    li.innerHTML="paul replaced pete"
    //add/delete 
    let newdiv=documentquerySelectorlet newTextNode=document.creatorTextNode




 
<body>
<html>
 <script>
//exo d'appl 2
<html>
<body>
  <div id="container">Users:</div>
  <ul class="list">
    <li>John</li>
    <li>Pete</li>
  </ul>
  <ul class="list">
    <li>Sarah</li>
    <li>Dan</li>
  </ul>
  <script>
   let list_ul= documentgetElementByclassName('list')
     for(let list of list_ul){
     for (let elment of listchilnodes){//pour avoir acces a chacun des enfants c'est childnotes
 
      console.log(list.(element.innertext))

//acessing to the first element of each ul ie john and sarah
//apres le premier for on peut mettre
console.log(list.firstElementChild) 
</script>
</body>
</html>



