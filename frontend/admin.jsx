const key = prompt("Admin Key");

fetch("/api/admin/stats", {
  headers: { "X-Admin-Key": key }
})
.then(r => r.json())
.then(d => {
  ReactDOM.createRoot(document.getElementById("root")).render(
    React.createElement("div", null,
      React.createElement("h1", null, "Admin Dashboard"),
      React.createElement("p", null, "Users: " + d.users),
      React.createElement("p", null, "Tokens: " + d.tokens),
      React.createElement("p", null, "Referrals: " + d.referrals),
    )
  );
});
