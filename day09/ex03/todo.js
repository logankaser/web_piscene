(()=>{
let s = document.cookie.match(RegExp('(?:^|;\\s*)todo_list=([^;]*)'));
s = s ? s[1] : null;
let list = [];
if (s) {
	list = JSON.parse(unescape(s));
	list.forEach(new_item);
}

function new_item(txt) {
	const ft_list = $("#ft_list");
	const item = document.createElement("div");
	item.innerText = txt;
	item.className = "Ta(c) Ff(m) C(#191919) Fz(s1) P(.5rem) " 
	item.className += (ft_list.children().length % 2 == 0) ? "Bgc(grey-7)" : "Bgc(grey-8)";
	item.onclick = e => { e.target.remove() };
	ft_list.prepend(item);
}

$("#new").click(() => {
	const txt = window.prompt("new todo:");
	if (txt != "") {
		new_item(txt);
		list.push(txt);
		document.cookie = "todo_list=" + escape(JSON.stringify(list));
	}
});
})();
