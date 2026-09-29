
(function(){
"use strict";
if(typeof CLASSES==='undefined')return;

var host=document.getElementById('sched');
if(!host)return;
var DAYS=[['MON','Monday'],['TUE','Tuesday'],['WED','Wednesday'],['THU','Thursday'],
          ['FRI','Friday'],['SAT','Saturday'],['SUN','Sunday']];
var day=host.dataset.day||'MON';
var view='studio';

function dayName(k){for(var i=0;i<DAYS.length;i++){if(DAYS[i][0]===k)return DAYS[i][1];}return k;}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');}
function val(id){var e=document.getElementById(id);return e?(e.type==='checkbox'?e.checked:e.value):'';}

var daysEl=document.getElementById('days');
if(daysEl){
  daysEl.innerHTML=DAYS.map(function(d){
    return '<button class="tab" role="tab" data-day="'+d[0]+'" aria-selected="'+(d[0]===day)+'">'+d[1]+'</button>';
  }).join('');
  daysEl.addEventListener('click',function(e){
    var b=e.target.closest('.tab');if(!b)return;
    day=b.dataset.day;
    [].forEach.call(daysEl.children,function(x){
      x.setAttribute('aria-selected',String(x.dataset.day===day));});
    render();
  });
}
var viewEl=document.getElementById('view');
if(viewEl){
  viewEl.addEventListener('click',function(e){
    var b=e.target.closest('button');if(!b)return;
    view=b.dataset.view;
    [].forEach.call(viewEl.children,function(x){
      x.setAttribute('aria-pressed',String(x.dataset.view===view));});
    render();
  });
}
['f-genre','f-teacher','f-level','f-loc','f-beg','f-term'].forEach(function(id){
  var e=document.getElementById(id); if(e) e.addEventListener('change',render);
});

function match(x){
  var g=val('f-genre'),t=val('f-teacher'),lv=val('f-level'),lo=val('f-loc'),beg=val('f-beg');
  if(x.day!==day)return false;
  if(g&&x.genre!==g)return false;
  if(t&&x.teacher!==t)return false;
  if(lv&&x.level!==lv)return false;
  if(lo&&STUDIO[x.studio].loc!==lo)return false;
  if(beg&&!(x.level==='Beginner'||x.level==='Open'))return false;
  return true;
}

function card(x){
  return '<div class="cls"><h4><a href="'+BASE+'dance-styles/'+x.slug+'.html">'+esc(x.name)+'</a></h4>'+
    '<div class="meta"><span class="tag lv">'+x.level+'</span><span class="tag">'+x.age+'</span>'+
    '<span class="tag">'+x.genre+'</span></div>'+
    '<p class="who"><b>'+x.teacher+'</b> &middot; '+x.start+'&ndash;'+x.end+'</p>'+
    '<div class="row"><a class="btn btn-primary btn-sm" href="'+BASE+
    'classes.html#trial">Book a trial</a></div></div>';
}

function render(){
  var rows=CLASSES.filter(match);
  if(!rows.length){
    host.innerHTML='<p class="empty">No classes match these filters on '+dayName(day)+
      '. Try another day or clear a filter.</p>';
    return;
  }
  var studios=STUDIOS.filter(function(s){
    var lo=val('f-loc'); return !lo||STUDIO[s].loc===lo;
  });
  var times=[];
  rows.forEach(function(x){if(times.indexOf(x.start)<0)times.push(x.start);});
  times.sort();

  var h;
  if(view==='week'){
    h='<table class="sched"><thead><tr><th class="time-col">Time</th><th>Class</th></tr></thead><tbody>';
    times.forEach(function(t){
      var cell=rows.filter(function(x){return x.start===t;});
      h+='<tr><td class="time">'+t+'</td><td>'+cell.map(card).join('')+'</td></tr>';
    });
    h+='</tbody></table>';
  }else{
    h='<table class="sched"><thead><tr><th class="time-col">Time</th>'+
      studios.map(function(s){return '<th>'+STUDIO[s].name+' &middot; '+STUDIO[s].loc+'</th>';}).join('')+
      '</tr></thead><tbody>';
    times.forEach(function(t){
      h+='<tr><td class="time">'+t+'</td>';
      studios.forEach(function(s){
        var cell=rows.filter(function(x){return x.start===t&&x.studio===s;});
        h+='<td>'+cell.map(card).join('')+'</td>';
      });
      h+='</tr>';
    });
    h+='</tbody></table>';
  }
  host.innerHTML=h;
}
render();
})();
