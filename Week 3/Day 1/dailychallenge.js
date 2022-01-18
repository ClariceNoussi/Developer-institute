let solar_system= [  // on a  un array qui contient 8 objects a une proprite dont la valeur rest un autre objet
{'Mercury':{'moons':0, "color":'orangedred'}}
 {'Venus':{'moons':0'color':'lightgrey'}}
 {'Earth':{'moons':1 'color':"lightseagreen"}}
  {'Mars':{'moons':2 'color':'red'}}
   {'Jupiter': {'moons':79 'color':'yellowgreen'}}
   {'Saturn':{'moons':62 'color':'violet'}}
    {'Uranus':{moons:82, 'color':'yellow'}}
     {'nepturne':{'moons':40, 'color':'darcyan'}}
    ]

solar_system[4]['jupiter']['moons']
let Planet_section=document.queryselector'section'

for(let planet of solar_system){
	let planet_div=document.createElement('div')
	planet_div.setAttribute("class", "planet")//or
	planet_div.classlist.add('planet', planet) // le second correspond aux elements de l'array qui apparaitront tour a tour
	planet_section.appendchild(planet_div)

}

//bonus
for(let planet_object=0; planet_object<solar_system.length; planet_object++ ){  //cette boucle nous aide a atteindre le nom de la planet
	console,log(planet_object)
	for(let planet in solar_system[])
									

//ceci c'est pour la boucle al'interieur de chaque objet
}