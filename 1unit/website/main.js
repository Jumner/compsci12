window.onload = () => {
	// Comment Code
	const codes = [...document.getElementsByClassName('code')];
	console.table(codes);
	// CSS
	codes
		.filter(code => {
			return code.classList.contains('css');
		})
		.forEach(code => {
			const lines = [...code.getElementsByTagName('span')];
			lines.forEach(line => {
				line.innerHTML = line.innerHTML
					.replace('/*', '<span class="comment">/*')
					.replace('*/', '*/</span>');
				console.log(line.innerHTML);
			});
		});
};
