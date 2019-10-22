

from behave import given
from behave import when
from behave import then

from behave import runner

class ASimpleClass:
	"""A simple class to help revise your knowledge on testing with Behave."""

	def __init__(self):
		self._lower_number = int() 
		self._higher_number = int()

	def init_a_simple_class(
		self,
		lower_number: int,
		higher_number: int
	) -> bool:
		"""Initialize the class's local variables.

		:param: lower_number: The lower of the two numbers.
		:param:	higher_number: The higher of the two numbers.
		:return: True if lower_number is lower than higher_number
			and Fsalse if not.
		"""
		self._lower_number = lower_number
		self._higher_number = higher_number
		if (lower_number > higher_number) or (lower_number == higher_number):
			self._lower_number = None
			self._higher_number = None
			print('Error : The higher_number variable must be higher than the lower_number variable')
			return False

		print('lower_number : %d\nhigher_number : %d\n' % (self._lower_number, self._higher_number))
		return True


	def values_assigned(self) -> bool:
		"""Assert that the values for _lower_number and _higher_number were assigned.
		
		:return True if the values were assigned correctly
			and False otherwise.
		"""
		if self._lower_number is None or self._higher_number is None:
			print('Error : _lower_number and _higher_number were not assigned correctly.')
			return False
		return True


	def change_the_lower_number_to(self, new_number: int) -> None:
		"""Change the _lower_number to a different value.

		:param: new_number: The new number to reassign self._lower_number to.
		"""
		if self.values_assigned() is not True:
			return

		print('Assigning self._lower_number from %d to %d\n' % (self._lower_number, int(new_number)))
		self._lower_number = int(new_number)


	def compare_lower_and_higher(self) -> str:
		"""Assert that the new value of self._lower_number is smaller, equal to or greater
		than self._higher_number.
		
		:return: 'LOWER' if nw the value of _lower_number is lower;
			'EQUAL' if new the value of _lower_number is equeal to _higher_number,
			'GREATER' if the new value of _lower_numberiis greater than _higher_number.
		"""
		if self._lower_number is None or self._higher_number is None:
			return 'VALUES NOT SET'
		if self._lower_number < self._higher_number:
			return 'LOWER'
		elif self._lower_number == self._higher_number:
			return 'EQUAL'
		else:
			return 'HIGHER'


@given(u'the user creates a new object with the lower number {lower_number} and '
		 'the higher number {higher_number}')
def step_impl(context: runner.Context, lower_number: str,
			  higher_number:str) -> None:
	"""Creates the class and assignes 

	:param: context: The global context object.
	:param: lower_number: The lower of the two numbers to be set
		in the object.
	:param: higher_number: The highest of the two numbers to be set
		in the object.
	"""

	context.simple_class = ASimpleClass()

	context.simple_class.init_a_simple_class(
		int(lower_number),
		int(higher_number)
	)



@when(u'the lower_number is changed to {new_lower_number}')
def step_impl(context: runner.Context,
			  new_lower_number: str) -> None:


	context.simple_class.change_the_lower_number_to(new_lower_number)


@then(u'the string printed out to the terminal is {string}')
def step_impl(context: runner.Context, string: str) -> None:


	assert context.simple_class.compare_lower_and_higher() == string











