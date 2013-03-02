/* index.js

This file is main javascript file for the NITS simulator.

It's purpose is to pass commands from the end user to the Python views.

v0.1 - index.js acts as a state machine to continually check for passengers and insert passenger trips
in the Python views.

*/

//Global Variables
var seconds; //The number of seconds into the simulation.
var gen_passengers = false; //If true, we are waiting for Python to return from Generating Passengers
var ready_to_ins_trips = false; //If true, we have finished generating passengers and are ready to insert trips into the system
var ins_trips = false; //If true, we are waiting for Python to return from inserting trips into the system

//TODO, where should these be declared?
var passenger_count;
var ready_trips;

/*generate_passengers
This function takes returns a set of passengers requesting trips at a particular second in the simulation
@parms
second: the current time into the simulation.  used to pull passengers from survey data
passengers_per_second: the rate at which passengers arrive, it is used when generating random sample data
simulation_code: future feature that will allow the database to maintain a total count of passengers across multiple simulations
*/
function generate_passengers(passengers_per_second, simulation_code, second){
    var passenger_count;
    console.log('waiting to generate passengers...');
    gen_passengers = true;
    $.ajaxSetup({async:true});
    $.post('/generate_passengers/', {passengers_per_second:passengers_per_second, simulation_code:simulation_code, second:second},
	   function(data){
	       var html_data = $('#infoWindow').html(); 
	       var message = $.parseJSON(data);
	       passenger_count = message['passengers'];
	       seconds = message['second'];
	       ready_trips = message['ready_trips'];
	       gen_passengers = false;
	       if(passenger_count > 0)
		   ready_to_ins_trips = true;
	   }
	  );
    console.log('passenger generation complete.');
    return [passenger_count, seconds, ready_trips]
}

function clear_old_data(){
    var html_data = $('#infoWindow').html(); 
    $('#infoWindow').html(html_data + '<br>Clearing Old Data...');
    $.ajaxSetup({async:false});
    $.post('/clear_old_data/',
	   function(data){
	       var message = $.parseJSON(data);
	       simulation_code = message.simulation_code
	       html_data = $('#infoWindow').html();
	       $('#infoWindow').html(html_data + '<br>Finished Clearing Old Data, simulation code iss: ' + message.simulation_code);
	       }
	  );
}

function insert_trips(second, trip_id){
    ins_trips = true;
    var opt_rte;
    var locations;
    var flexbus_id;
    var home;
    var html_data = $('#infoWindow').html(); 
    console.log(trip_id);
    console.log(ready_to_ins_trips);
    var trip_ids;
    trip_ids = JSON.stringify(trip_id);
    console.log(trip_ids);
    $('#infoWindow').html(html_data + '<br>Current Time is ' + second + ' seconds.');   
    console.log('Inserting trips at time ' + second);
    $.ajaxSetup({async:true});
    $.post('/insert_trip/', {"second":second, "trip_ids":trip_ids},
	   function(data){
	       var message = $.parseJSON(data);
	       console.log(message);
	       opt_rte = message['opt_rte'];
	       locations = message['locations'];
	       ins_trips = false;
	   }
	  );
    return opt_rte;
}

/*
Setup the simlation                                                                                                                                           
Set parameters for lengh of simulation, 
*/                            
var simulation_code;
var simulation_length = .1*3600;
var passengers_per_second = .05;

console.log("Begin the simulation...");
clear_old_data();
console.log("The simulation code is...");
console.log(simulation_code);

var master_interval = setInterval(function(){master()},100);
var trip_index = 0;
var result;
result = generate_passengers(passengers_per_second, simulation_code, 0);

function master(){
    var last_time = false;
    if (seconds > simulation_length){
	last_time = true;
	var html_data = $('#infoWindow').html(); 
	$('#infoWindow').html(html_data + '<br>This is the last time that the script will run.  The simulation is over...');  
    }

    if(gen_passengers)
	console.log('Generating passengers...waiting...');
    else{
	if(ready_to_ins_trips){
	    ready_to_ins_trips = false;
	    insert_trips(seconds, ready_trips);
	    console.log('Calling inserting trips');
	}
	else{
	    if(ins_trips)
		console.log('Inserting Trips...waiting...');
	    else{
		ready_trips = [];
		console.log('done inserting trips.  Ready to move on to the next second');
		if(last_time){
		    console.log('these passengers will never be inserted');
		    clearInterval(master_interval);
		}
		else{
		    seconds = seconds + 1;
		    console.log(seconds);
		    console.log(passenger_count);
		    result = generate_passengers(passengers_per_second, simulation_code, seconds);
		}
	    }
   
	}
    }
}

console.log("The Great Loop is Finished");

