let addressNumber= "677";
let addressStreet ="Nsimeon";
let country ="Cameroon";

//2
let globalAddress = "I live in " +addressNumber +" "+ addressStreet+ 
", in "+ country ;

//3
console.log(globalAddress)

//Exercice 2

let birth_year = 1985;
let future_year = 2035 ;
let future_age = future_year - birth_year ;
console.log("I will be "+future_age +" in "+future_year);

//Exercice 6

let str1 = "mix"
let str2 = "pod"
// pox mid
let new_word= str2.substring(0,2)+str1.substring(2)+" "+
str1.substring(0,2)+str2.substring(2)
alert(new_word)

//example 2
let a = "Hello"
let b = "World"

//Worlo Held
let c = b.substring(0,4)+a.substring(4)+" "+a.substring(0,2)+b.substring(3)
alert(c)

//Exercice 7

let num1 = parseFloat(prompt("Enter the first number :"))
let num2 = parseFloat(prompt("Enter the second number :"))
let operator = prompt("Enter the operation sign:")

let sum =num1+num2

alert(`The sum is ${sum}`)
let result = eval(num1+ operator+ num2) // nombre + un signe + un nombre
alert("The result is "+result)

//Exercice Nemo
//let sentence = prompt("Hey enter a sentence with Nemo :")
let index = sentence.indexOf("Nemo")
alert("I find Nemo at position "+ index)

let array_s = sentence.split(" ")
let index2 = array_s.indexOf("Nemo")
alert("I find Nemo at position "+ index2)

//Ask the numbers

let numbers = prompt("Enter numbers separated by commas : ")

let array_number = numbers.split(",")
let produit =  array_number.reduce((a,b)=>a*b)
console.log("The product is "+produit)


//example dans la console pour les fonctions du UI
let name = prompt("What's your name ?")
undefined
name
"Alexandra"
let first_name = prompt("Whats your first name ?")
undefined
first_name
"Jane"
let full_name =name + first_name
undefined
full_name
"AlexandraJane"
full_name =name +' '+ first_name
"Alexandra Jane"
confirm("Is your full name "+ full_name + " ?")
true
alert("Congratulations")






