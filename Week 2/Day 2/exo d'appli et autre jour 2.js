let info=prompt("Entrez votre prenom et votre age separes par 'de'")
//seulement nom et age
let a =info.split ("de") 
//DEmander nom de famill
let family_name =prompt("Entrez votre nom de famille")
	a.push("surname")
//Nom complet
let full_name= a[0]+" "+a[2]
demande de valider son nom
confirm("Is" +full_name+ "your full name?")
true

//age de 2015
//acceder a l'age utiliser substring pour decouper et 1 car c'est 'espace qui a l'index 1 pour obtenir age sans ans a la suite
a[1].substring(0.1)
let actual_age=a[1]
let age_2015=actual_year-6
console.log("Your were" + age_2015+''+"in"+"2015")

 //determiner s'il est major au cameroon
 if (age_number>=21){
 	alert("vous etes majeur au Cameroun")
 } else{
 	alert("voyagez dans un autre pays pour etre majeur")

 }

 //exo 1 des exos du cours
 let x=10
 let y=4
if (x>y){
	alert(x+" is the biggest number")
}else{
	alert(x+"is the smallest number")
}
//Exo 2
let newdog="Chihuahua"
let lettercount=newdog.length
alert("the word Chihuahua has "+ lettercount+' '+"letters")
newdog.toLowerCase()
newdog.toUpperCase()

if (newdog=="Chihuahua"){
	alert ("I love chihuahua, it’s my favorite dog breed")
}else{
	console.log ("I dont care, I prefer cats")
}
//Exo 3
let x=prompt("enter a number..")
if (x%2==1){
	alert(x+"is an odd number")
}else if (x%2==0){
	alert(x+"is an even number")
}

//exo 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
let numberofusers=prompt('enter the number of users online')
if (numberofusers==0 ){
	alert("no one is online")
}else if (numberofusers==1){
	alert(users[0]+"is online")
}else if (numberofusers==2){
	alert(users[0,0]+ "and"+users[0,1]+ "are online")
}else if (numberofusers>2){
alert(users[0,0]+ ","+ users[0,1]+ users.length-2+"are online")
}


//Daily challenge peut on gerer aveclet sentence_array=sentence.split(' ')
let sentence="the movie is not that bad , I like it"
sentence.length
let wordnot=sentence.substring(14)
let wordbad=sentence.substring(23)
//replace not that bad par good
if (wordnot before wordbad){
	alert(sentence.splice(14,23)+"good")
}
//exo daily challenge correction prof
let sentence="the movie is not that bad, I like it"
let arr=sentence.split(" ")
let wordnot=arr.indexOf('not')
let wordbad=arr.indexOf("bad")
if (wordnot>wordbad){
	arr.splice(wordnot, worbad-wordbad+1, "good")
let new_sentence=arr.join(" ") //pour ajouter le nouveau mot (good) dans l'array precedent
 alert(new_sentence)
} else{(sentence)}


//exo 1 xp gold
let language=prompt("what language do you speak")
language.toLowerCase()


//exo 2 xp gold


//exo 3 xp gold
let verb=prompt("Please enter a verb")
if (verb.length>=3 && verb.endwith==false){
	alert(verb + "ing")
} else if(verb.length>=3, verb.endwith("ing")==true){
	alert(verb+"ly")
}else if (verb<3){
    alert( "try another verb")
}

//LOOPS
//Exo 1 d'appli cours

For(let i= 0; i < 15; i++){

	if (i % 2==0){console.log(i+"is odd")}else{console.log(i+"is even")}
}
//nombre de chiffre impair entre 1900-1920
for(let i=1900; i<1920;i++){if (i % 2==!0){console.log(i+"is odd")}else{console.log(i+"is even")}


//Exo 2 d'appli cours
