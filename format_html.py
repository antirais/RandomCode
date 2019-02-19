"""
Basic str formatter to escape data in HTML
"""

import string
import html

class HTMLFormatter(string.Formatter):
	def format_field(self, value, format_spec):
		if format_spec == 'ht':
			return html.escape(value)

		elif format_spec == 'hp':
			return f'"{html.escape(value)}"'

		elif format_spec == 'hpjs':
			if value.lower().startswith('javascript'):
				value = value[len('javascript'):]
			elif value.lower().startswith('data'):
				value = value[len('data'):]

			if value.startswith(':'):
				value = value[1:]

			value = value.replace('\\', '\\\\')
			value = value.replace('/', '\\/')
			value = value.replace("'", "\\'")
			value = value.replace('"', '\\"')
			value = value.replace('\n', '\\n')
			return f'"{html.escape(value)}"'

		elif format_spec == 'js':
			value = value.replace('\\', '\\\\')
			value = value.replace('/', '\\/')
			value = value.replace("'", "\\'")
			value = value.replace('"', '\\"')
			value = value.replace('\n', '\\n')
			return f'"{value}"'

		return super().format_field(value, format_spec)

if __name__ == '__main__':
	fmt = HTMLFormatter()
	print(fmt.format(
		'''
		<b>{:ht}<b><img src={:hp} onerror={:hpjs} style={:hcss}>
		<script>
		var x = {:js};
		</script>
		''',

		'<img src="x" onerror=alert(1)>',
		'zxc`\"\\\'></&',
		'DATA:\\u0061lert("1&", \'tests\')//\n</script>',
		'url("javascript:alert(1)")',
		'DATA:\\u0061lert("1&", \'tests\')//\n</script>',
	))
