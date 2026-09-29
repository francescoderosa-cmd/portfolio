
(function(){
"use strict";
var sel=document.getElementById('m-item');
var form=document.getElementById('reserve-form');
if(!sel||!form)return;

/* "Reserve" on a card preselects that item and moves you to the form */
document.addEventListener('click',function(e){
  var b=e.target.closest('[data-reserve]');
  if(!b)return;
  var want=b.getAttribute('data-reserve');
  for(var i=0;i<sel.options.length;i++){
    if(sel.options[i].text===want){sel.selectedIndex=i;break;}
  }
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  form.scrollIntoView({behavior:reduce?'auto':'smooth',block:'center'});
  /* let the scroll settle before pulling focus, or the browser jumps twice */
  setTimeout(function(){sel.focus({preventScroll:true});},reduce?0:420);
});
})();
