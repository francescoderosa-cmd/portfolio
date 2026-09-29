
(function(){
"use strict";

/* ---- promo banner ---- */
var promo=document.getElementById('promo');
if(promo){
  try{ if(sessionStorage.getItem('as-promo')==='off') promo.hidden=true; }catch(e){}
  var pc=promo.querySelector('button');
  if(pc) pc.addEventListener('click',function(){
    promo.hidden=true;
    try{ sessionStorage.setItem('as-promo','off'); }catch(e){}
  });
}

/* ---- nav dropdowns ---- */
var items=[].slice.call(document.querySelectorAll('.nav-item.has-drop'));
items.forEach(function(it){
  var btn=it.querySelector('button');
  function open(v){
    it.classList.toggle('open',v);
    btn.setAttribute('aria-expanded',v?'true':'false');
  }
  it.addEventListener('mouseenter',function(){open(true);});
  it.addEventListener('mouseleave',function(){open(false);});
  btn.addEventListener('click',function(e){
    e.stopPropagation();
    var was=it.classList.contains('open');
    items.forEach(function(o){o.classList.remove('open');
      var b=o.querySelector('button'); if(b) b.setAttribute('aria-expanded','false');});
    open(!was);
  });
  it.addEventListener('keydown',function(e){ if(e.key==='Escape') open(false); });
});
document.addEventListener('click',function(){
  items.forEach(function(o){o.classList.remove('open');
    var b=o.querySelector('button'); if(b) b.setAttribute('aria-expanded','false');});
});

/* ---- mobile menu ---- */
var burger=document.getElementById('burger'),mobile=document.getElementById('mobile');
if(burger&&mobile){
  burger.addEventListener('click',function(){
    var open=mobile.classList.toggle('open');
    burger.setAttribute('aria-expanded',open?'true':'false');
    burger.setAttribute('aria-label',open?'Close menu':'Open menu');
  });
  mobile.addEventListener('click',function(e){
    if(e.target.tagName==='A'){mobile.classList.remove('open');
      burger.setAttribute('aria-expanded','false');}
  });
}

/* ---- reveal on scroll ---- */
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var els=document.querySelectorAll('.rv');
if(reduce||!('IntersectionObserver' in window)){
  [].forEach.call(els,function(el){el.classList.add('in');});
}else{
  var io=new IntersectionObserver(function(en){
    en.forEach(function(e){ if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);} });
  },{rootMargin:'0px 0px -8% 0px',threshold:.06});
  [].forEach.call(els,function(el){io.observe(el);});
}

/* ---- mailto forms ---- */
[].forEach.call(document.querySelectorAll('form[data-mailto]'),function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var to=f.getAttribute('data-mailto');
    var subj=f.getAttribute('data-subject')||'Website enquiry';
    var lines=[];
    [].forEach.call(f.querySelectorAll('input,textarea,select'),function(el){
      if(!el.name||el.type==='submit')return;
      var lab=f.querySelector('label[for="'+el.id+'"]');
      lines.push((lab?lab.textContent.trim():el.name)+': '+el.value);
    });
    window.location.href='mailto:'+to+'?subject='+encodeURIComponent(subj)+
      '&body='+encodeURIComponent(lines.join('\n'));
  });
});

/* ---- share buttons ---- */
[].forEach.call(document.querySelectorAll('[data-share]'),function(box){
  var url=location.href, title=document.title;
  var map={
    x:'https://twitter.com/intent/tweet?url='+encodeURIComponent(url)+'&text='+encodeURIComponent(title),
    facebook:'https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(url),
    linkedin:'https://www.linkedin.com/sharing/share-offsite/?url='+encodeURIComponent(url),
    whatsapp:'https://wa.me/?text='+encodeURIComponent(title+' '+url)
  };
  [].forEach.call(box.querySelectorAll('a[data-net]'),function(a){
    a.href=map[a.getAttribute('data-net')]||url;
  });
  var copy=box.querySelector('[data-copy]');
  if(copy) copy.addEventListener('click',function(){
    var done=function(){
      var m=box.querySelector('.copied');
      if(m){m.textContent='Link copied';setTimeout(function(){m.textContent='';},2200);}
    };
    if(navigator.clipboard) navigator.clipboard.writeText(url).then(done,done); else done();
  });
});

/* ---- generic chip filters (data-filter-group / data-filter-target) ---- */
[].forEach.call(document.querySelectorAll('[data-filter-group]'),function(group){
  var target=document.querySelector(group.getAttribute('data-filter-group'));
  if(!target)return;
  group.addEventListener('click',function(e){
    var b=e.target.closest('.chip'); if(!b)return;
    var on=b.getAttribute('aria-pressed')==='true';
    [].forEach.call(group.querySelectorAll('.chip'),function(c){c.setAttribute('aria-pressed','false');});
    b.setAttribute('aria-pressed',on?'false':'true');
    var want=on?'':b.dataset.value;
    var shown=0;
    [].forEach.call(target.children,function(card){
      var tags=(card.dataset.tags||'').split('|');
      var ok=!want||tags.indexOf(want)>=0;
      card.style.display=ok?'':'none';
      if(ok)shown++;
    });
    var msg=document.querySelector('[data-filter-empty]');
    if(msg) msg.hidden=shown>0;
  });
});

/* ---- simple tab groups (data-tabs) ---- */
[].forEach.call(document.querySelectorAll('[data-tabs]'),function(bar){
  bar.addEventListener('click',function(e){
    var t=e.target.closest('.tab'); if(!t)return;
    [].forEach.call(bar.querySelectorAll('.tab'),function(x){x.setAttribute('aria-selected','false');});
    t.setAttribute('aria-selected','true');
    var name=t.dataset.panel;
    [].forEach.call(document.querySelectorAll('[data-panel-for="'+bar.dataset.tabs+'"]'),function(p){
      p.hidden=p.dataset.panel!==name;
    });
  });
});
})();
