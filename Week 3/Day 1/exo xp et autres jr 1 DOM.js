<!Doctype>
<html>
<body>

<div id="navBar">
    <ul>
        <li><a href="#">Profile</a></li>
        <li><a href="#">Home</a></li>
        <li><a href="#">My Friends</a></li>
        <li><a href="#">Messenger</a></li>
        <li><a href="#">My Pics</a></li>
    </ul>
</div>
<script>
//change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method
let newdiv=document.getElementById('navbar')
newdiv.setAttribute ("id", "socialNetworkNavigation")

//add new 'li'add append text node and update list
      let newli2 = document.createElement('li')  
      let newTextNode = document.createTextNode('logout')
      newtexnode
     
      newli2.appendChild(newTextNode)
      let ul=newdiv.FirstElementChild
      ul.appendChild(newli2)

      //bonus
let new_list1= ul.removeFirstElementChild('li') && ul.removeLastElementChild ('li')

console.log(new_list.textcontent)

</script>
</body>


</html>