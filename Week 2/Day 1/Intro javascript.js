let addressNumber="677"
let AddressStreet="Nsimeyong"
let country="Cameroon"

//2
let globalAddress = "I live in "+ addressNumber+" "+ AddressStreet +"in" + country

//exo 2 
console.log(globalAddress)

let birth_year=1989;
let future_year=2022
let future_age= future_year - birth_year

console.log("I will be "+ future_age+" "+"in"+" "+future_year)

// exo xx1
let str1="mix"
let str2="pod"
let new_word= str2.substring(0,2)+str1.substring(2)+" "+str1.substring(0,2)+str2.substring(2)
alert(new_word)

// exo xx2
let a="hello"
let b="world"
// worlo held
let c=b.substring


//Exo calculator
let num1=parsefloat(prompt("enter the first number:"))
let num2= parsefloat(prompt('enter the second number:'))
let sum=num1+num2
alert("the sum is $(sum)")

//autre exemple dans le meme sens avec les meme var precedents et en plus...

	let operator=prompt("enter the operation sign:")


let result=eval(num1+operator+num2)
alert("The result is"+result)




