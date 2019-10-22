
Feature: A simple behave test

	Scenario Outline: Testing ASimpleClass using Behave
		Given the user creates a new object with the lower number <lower number> and the higher number <higher number>
		When the lower_number is changed to <new lower number>
		Then the string printed out to the terminal is <string>

		Examples:
		| lower number | higher number | new lower number | string         |
		| 42		   | 88			   | 12				  | LOWER  		   |
		| 77		   | 20			   | 12				  | VALUES NOT SET |
		| 10		   | 45            | 50               | HIGHER		   |
		| 1			   | 42 		   | 42				  | EQUAL		   | 
