//exo d'appl 1
function calcul_age(myage){
let mum_age=myage*2
let dad_age=agemum*1.2

console.log(my mum age is ${mum_age} years old and my dad is {dad_age} years old)}

//exo 2
function calculate_age(myage){

if (mum_age=myage*2){
	let result="my mum is twice my age"
return result
} else{
	return"that's not my mum age"
}
 
 //expl integrant arrow function
 const calcul_age= (myage)=>{sentence=my mum age is ${mum_age} years old and my dad is {dad_age} years old; return sentence}

 //appl sur CALLBACK
 var show_info=(name1, name2){
 console.log(name1); setTimeout(say_hello, 5000)} //5mil= temps en miliseconde donc 5 secondes suite a chercher

//exo xp
//Part I
function infoaboutme(){
	
console.log("My name is Clarice, I'm 21 years ols and i love computer sciences")
}
//call the function
infoaboutme()

//Part II
function infoAboutPerson(personName, personAge, personFavoriteColor)

	console.log("your name is"+personName+ "you are "+personage+"years old, your favorite color is"+personFavoriteColor)
}
//Part II :call the function
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")
 //Part III
 function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies){
 	console.log("your name is"+personName+ "you are "+personage+"years old, your favorite color is"+personFavoriteColor+"you love"+personHobbies)}


//tout dans une phrase
function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies){
	let hobby_string
	For(i in personHobbies){

	if(i==0){
		hobby_string=persoHobbies[0] //on peut mettre i mais i est deja defini comme zero et ici on veut qu'il n'yait pas de virgule avant le premier element

	}else if(i==personHobbies.length-1){
		hobby_string+="and"+personHobbies[i]
	}else if {hobby_string+=","+personHobbies[i]}
	}
	console.log(hobby_string)
 		
console.log(console.log("your name is"+personName+ "you are "+personage+"years old, your favorite color is"+personFavoriteColor+"you love"+hobby_string))
}
//call function
infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

//Exo 2
let userage=prompt('please enter your age her..')
function checkdriverage (userage){
		if (userage<18){
		console.log("Sorry, you are too young to drive this car. Powering off")
}else if(userage==18){
	console.log("You are old enough to drive, Powering On. Enjoy the ride!")
} else if (userage>18){
			console.log('Congratulations on your first year of driving. Enjoy the ride')}
	}

//call the function
checkdriverage(30)

//exo 3
function checkNumber(){

    for(i=0; i<100; i++){
	if (i%2==0){
		console.log('the'+ i + 'is an even')
	}else if(i%2!=0){
		console.log("the"+ i+ "is an odd")}

	}
}

//call the function
checkNumber()

//daily challenge
let word=prompt('please enter severals words separated by commas..')
let array=word.split()
let longest_word=0
for (let i=0; i<array.length; i++){
	if(array[i].length>longest_word.length){
		longest_word=array[i]
	}        
 }
console.log(longest_word)
let nbr_stars=longest_word.length+4 //dans l'expl, on avait hello qui a 5lettres pour 9 etoile, 4 represente la difference.
let star_line= '*'.repeat(nbr_stars)// on peut mettre juste le signe de la multiplication a la place de repeat, car tout string suivi de * et un nombre, le me repete automatiquement "a"*2="aa"
let margin_rigth= (longest_word.length-array[i])+1  // pour definir le nombre d'etoile restant pour chaque mot le plus long mot moins le mot considerer+ l'etoile de la marge de la fin
