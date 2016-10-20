from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell, new_output
from ipytail import IPyTail

class TestIPyTail:
	def test_tail(self):
		nb = new_notebook(cells=[new_code_cell(str(i)) for i in range(1, 50)])

		nb2 = IPyTail().tail(nb, 5)
		assert len(nb2['cells']) == 5

		expected_cells = [new_code_cell(str(i)) for i in range(45, 50)]
		assert nb2['cells'] == expected_cells

	def test_trim_output(self):
		trim_output = IPyTail()._trim_output
		output = new_output('stream', text=['1', '2', '3', '4', '5', '6'])
		output2 = trim_output(output, 4)
		assert output2 == new_output('stream', text=['1', '2', '...\n', '5', '6'])