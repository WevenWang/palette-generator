const form = document.getElementById("color-form");
form.addEventListener("submit", (e) => {
	e.preventDefault();
	getColors();
});

function getColors() {
	const color = form.color.value;
	fetch("/palette", {
		method: "POST",

		json: true,

		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ color }),
	})
		.then((res) => res.json())
		.then((data) => {
			const colors = data;

			const container = document.getElementById("color-container");

			container.innerHTML = "";
			createColorBoxes(colors, container);
		});
}

function createColorBoxes(colors, container) {
	for (const color of colors) {
		const div = document.createElement("div");
		div.classList.add("color");
		div.style.backgroundColor = color;
		div.style.width = `calc(100% / ${colors.length})`;

		div.addEventListener("click", () => {
			navigator.clipboard.writeText(color);
		});
		const span = document.createElement("span");
		span.innerText = color;
		div.appendChild(span);

		container.appendChild(div);
	}
}
