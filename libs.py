from IPython.display import HTML

def hide_code():
    return HTML('''<script>
    code_show=true; 
    function code_toggle() {
    if (code_show){
    $('div.input').hide();
    } else {
    $('div.input').show();
    }
    code_show = !code_show
    } 
    $( document ).ready(code_toggle);
    </script>
    <form action="javascript:code_toggle()"><input type="submit" value="Clique para esconder/exibir script."></form>''')