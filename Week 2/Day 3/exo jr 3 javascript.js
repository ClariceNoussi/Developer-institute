//LOOPS
//Exo 1 d'appli cours

For(let i= 0; i < 15; i++){

	if (i % 2==0){console.log(i+"is odd")}else{console.log(i+"is even")}
}
//nombre de chiffre impair entre 1900-1920
for(let i=1900; i<1920;i++){if (i % 2==!0){console.log(i+"is odd")}else{console.log(i+"is even")}


//Exo 2 d'appli cours
//Q1
let names= ["john", "sarah", 23, "Rudolf",34]
for (let i=0; i<names.length; i++){      //on peut mettre i==names.length-1 aussi au 2e i

    if (typeof(names[i])!="string"){
    	continue

    }
    else if (typeof(names[i])=="string"){
	let first_letter=names[i].substring(0,1)
	if(first_letter.toUppercase()!=first_letter)}
		console.log(first_letter.toUpperCase()+names[i].substring(1))
}

//Q2
names.ForEach(item=>){    //si c'estait forEach names.ForEach(item=>), si for of =for(item of names) si for in for (items in names)
	if (typeOf(item)!=string {break}
	else if(typeOf(item)==("string"){console.log (item)}
}

For(item in names){
	if (typeOf(names[item]))
}

//Exo1 xp

let color=["blue", "orange", "green", "yellow", "white"]
for (let i=0; i<colors.length; i++){
	console.log("my"+(i+1)+ "choice is"+color[i])

//Q2 bonus
	 if (i==0){
	 	console.log("my first choice is"+color[i])}

	 if (i==1){
	 	console.log('my second choice is'+color[i])}

	 if(i==2){
	 	console.log('my third choice is'+color[i])}

	 	if(i>3){
	 		console.log('my'+ i+"th choice is"+color[i])}
}

//exo 2 xp
let people = ["Greg", "Mary", "Devon", "James"]
//remove Greg
people.shift( )
//james to jason

people.splice(2,1,"jason")

//my name at the end
people.push("clarice")
//iterate
let new_people=['Mary', 'devon', 'jason','clarice']
for (let n=0; n<new_people.length; n++){
	if (n==3)
		break// au moment ou doi apparaitre mon nom, il y'a break donc on est after jason
}
//slice array
let favorite = new_people.slice(1,3)

//indexof mary et appropos de foo
let indexMary=new_people.indexOf("Mary")
let indexMary2=new_people.indexOf("mary")
console.log(indexMary)
console.log(indexMary2)//Mary avec "m " en miniscule donne -1 ou chercher l'indice de mon nom dans favorite donne aussi -1. on doit faire quelque chose


//variable last
let last=new_people.push("last")
let indexlast=last.length-1


//Daily challenge
const numbers = [5,0,9,1,7,4,2,6,3,8]
//covert array to string with toString and join
let string_numbers=numbers.toString("")
let string_numbers2=numbers.join('+')
let string_numbers3=numbers.join(' ') //the good one according to me
let string_numbers4=numbers.join('')

//sort numbers in descending order (on va utiliser 2 loops)
const numbers = [5,0,9,1,7,4,2,6,3,8]
let temp; //variable pour garder les valeurs temporairement
  for ( i = 0; i < a.Length; i++) 
    {
        for ( j = 0; j <a.Length; j++) 
        {
            if (j != a.Length - 1)
            {
                if (numbers[n] < numbers[j + 1])
                {
                    temp = numbers[n];
                    numbers[j] = numbers[j + 1];
                    numbers[n + 1] = temp;
                }
            }

        }
        console.log=()

    }



//exo xp ninja
//create 2 object
let user1 ={
	Fullname : "Clarice",
	Mass:62
	Height:1.62
	BMI= function () {
		console.log('the BMI is' + user1.Mass / user1.Height^2)}
	}
	

let User2= {
	Fullname : "Michael"
	Mass:90
	Height:1.82
	BMI= function () {
		console.log('the BMI is' + user2.Mass/ user2.Height^2)}
}

Function compareBMI(){
if(user1.BMI () > user2.bmi()){
	console.log(user1.Fullname)}
} else{
	console.log(person2.Fullname)
}
}
