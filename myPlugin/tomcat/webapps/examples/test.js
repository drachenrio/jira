<script>
function myFunction() {
    var str = "http://www.jira.com/issue/rel-101";
    var n = str.lastIndexOf("/");
    var token = str.substring(n+1);
    token = token.toUpperCase();
    var startREL = token.startsWith("REL");
    var startNFR = token.startsWith("NFR");
    document.getElementById("demo").innerHTML = startREL;
}
</script>
