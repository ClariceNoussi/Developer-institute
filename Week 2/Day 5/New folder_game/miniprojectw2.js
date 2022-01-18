
//3-1 
function playTheGame(){
	let question=confirm('you would like to play the game, right?')
	if (question==false){
	alert('No problem, Goodbye')
	}
	let number=prompt('Enter a number between 0 and 10')
	let usernumber=Number(number)

      if (typeof(usernumber)!="number"){
			alert('Sorry Not a number, Goodbye')

		}
		else if(usernumber<0 ||usernumber>10){
			alert('Sorry it’s not a good number, Goodbye')
		}
		
		
			let computernumber=Math.round(Math.random()*10)	
				// let computernumber=Math.random()*10   //mathrandom donne tjrs les valeurs de zero virgule.... c'est pk on multiplie par 10 pour que ce soit compris entre 0 et 10
			// computernumber=Math.round() pour avoir nombre entier

			test(usernumber,computernumber)

}


//part II
function test(usernumber,computernumber){   //on peut mettre var (parametres )mais a la suite mettre la fleche=>

	let i=1;
  	do{								//do while permet d'effectuer une tache apres une autre je crois, i va de fois 0 a 3e fois

	if(usernumber==computernumber){
		alert("WINNER, congrats")
		break;
	}else if(usernumber>computernumber){
		alert("Your number is smaller than the computer’s, guess again")
		usernumber=Number(prompt('#'+i+"attempt; enter another number between 0 and 10"))

	}else if(usernumber<computernumber){
	alert ("Your number is smaller then the computer’s, guess again")
	usernumber=parseInt(prompt('#'+i+"attempt; enter another number"))
	}
	i++;
	}

	while (i<4){
		alert("Game over")}
	
}
			
	


