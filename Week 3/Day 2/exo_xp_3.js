//add a title
let title=document.createElement("h2")
let text=document.createElement(my shopping list)



//form and elements creation

let shoppingList=documentcreateElement('form')
let input= document.createElement('input')
let add_btn=document.createElement('button')
let div=document.getElementById('id')
input.setattribute()
 //adding rm and hiselements to the html
 form.appendchild(input)//on commence par les petits enfant qui ici sont input et button de form lui qui est fils unique de div
 form.appendchild(add_button)

 div.appendchild(form)

 //adding event to add the items in the array
 add_btn.addEventListener('click', additem)

 function additem(e){
 	let item= input.value //formule pour recuperer un input
 	if (item!=''){
 	shoppingList.push(item)//ici on veut ajouter un element (item) a un array
 	alert(item)
 	
 
 	input.value=''}
 	e.preventdefault() //empeche le navigateur d'actulaiser la page, ca ramene le code vers le debut et vide 
}
 console.log(shoppingList)
 //clearAll Button and event
 let clear_btn=document.creatElement('ul')// apres avoir creer chaque element, penser a la formule appendchild ensuite pour lier



//creating the list of our shopping