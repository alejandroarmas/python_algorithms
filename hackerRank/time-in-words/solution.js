'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
	    inputString += inputStdin;
});

process.stdin.on('end', _ => {
	    inputString = inputString.replace(/\s*$/, '')
	        .split('\n')
	        .map(str => str.replace(/\s*$/, ''));

	    main();
});

function readLine() {
	    return inputString[currentLine++];
}

const HOUR = 60;
const HALF_AN_HOUR = 30;
const HIT_THE_HOUR = 0;
const QUARTER = 15;

function map_number_to_string(number) {
	    
	    const NUMBER_STRING_MAP = ["", "one", "two", "three", "four",
		                            "five", "six", "seven", "eight",
		                            "nine", "ten", "eleven", "twelve",
		                            "thirteen", "fourteen", "quarter"];
	    
	    const UNIQUE_BASE_NUMBER_AMT = NUMBER_STRING_MAP.length;
	    const ones_place_digit = number % 10;
	    
	    let output = "";
	    
	    if (number < UNIQUE_BASE_NUMBER_AMT) {
		            output = `${NUMBER_STRING_MAP[number]}`; 
		        }
	    else if (number < HALF_AN_HOUR - 10){
		            output = `${NUMBER_STRING_MAP[ones_place_digit]}teen`     
		        }
	    else if (number < HALF_AN_HOUR){
		            output = `twenty ${NUMBER_STRING_MAP[ones_place_digit]}`
		        }
	    else if (number === HALF_AN_HOUR){
				output = "half";
		}
	    
	    return output;
}

function timeInWords(hour, minute) {
	    
	    const adjusted_minutes = (minute <= HALF_AN_HOUR ? minute : HOUR - minute);
	    let adjusted_minutes_string = map_number_to_string(adjusted_minutes);    
	    
	    if (adjusted_minutes === 1) {
		            adjusted_minutes_string += " minute";
				} else if (adjusted_minutes > HIT_THE_HOUR & adjusted_minutes !== QUARTER & adjusted_minutes !== HALF_AN_HOUR) {
					adjusted_minutes_string += " minutes";
				    }
	    
	    
	    if (minute === HIT_THE_HOUR) {
		            return `${map_number_to_string(hour)} o' clock`
		        }
	    else if (minute <= HALF_AN_HOUR) {
		            
		            return `${adjusted_minutes_string} past ${map_number_to_string(hour)}`;
		        }
	    else if (minute < HOUR){
		            return `${adjusted_minutes_string} to ${map_number_to_string(hour + 1)}`;
		        }
}

function main() {
	    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

	    const h = parseInt(readLine(), 10);

	    const m = parseInt(readLine(), 10);

	    let result = timeInWords(h, m);

	    ws.write(result + "\n");

	    ws.end();
}

