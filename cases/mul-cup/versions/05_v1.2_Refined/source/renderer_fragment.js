// Offline, procedural perspective glass preview. The product is rotationally symmetric;
// subtle etched lettering and lighting cues make horizontal rotation perceivable.
let rotator=null;
function makeRotator(){
 const stage=$('product-display');
 const canvas=document.createElement('canvas'); canvas.width=560;canvas.height=680;
 canvas.tabIndex=0;canvas.setAttribute('role','img');
 canvas.setAttribute('aria-label','클리어 컵 회전 보기. 좌우 방향키나 드래그로 회전할 수 있습니다.');
 stage.insertBefore(canvas,stage.querySelector('.rotate-hint'));
 stage.classList.add('rotatable-ready');
 const ctx=canvas.getContext('2d');if(!ctx){canvas.remove();stage.classList.remove('rotatable-ready');return null;}
 const state={yaw:.34,tint:'#b5dad2',name:'클리어',drag:false,x:0,y:0,pitch:.23,moved:false};
 const base=.34;
 const rAt=y=>105-(y-180)*.09;
 const proj=(theta,y)=>{
  const r=rAt(y);let x=r*Math.sin(theta+state.yaw),z=r*Math.cos(theta+state.yaw);
  const tilt=state.pitch;
  const vy=(y-366)*Math.cos(tilt)-z*Math.sin(tilt);
  const vz=(y-366)*Math.sin(tilt)+z*Math.cos(tilt);
  const f=1250/(1250+vz);
  return [280+x*f,365+vy*f];
 };
 function ellipse(y,frontOnly=false){
  ctx.beginPath();let first=true;
  for(let i=0;i<=96;i++){
    const a=frontOnly ? -Math.PI/2+Math.PI*i/96 : Math.PI*2*i/96;
    const [x,v]=proj(a,y);if(first)ctx.moveTo(x,v);else ctx.lineTo(x,v);first=false;
  }
 }
 function shellPath(){ctx.beginPath();const pts=[];
  for(let i=0;i<=36;i++){let y=180+(555-180)*i/36;pts.push(proj(Math.PI/2-state.yaw,y));}
  for(let i=36;i>=0;i--){let y=180+(555-180)*i/36;pts.push(proj(-Math.PI/2-state.yaw,y));}
  pts.forEach((p,i)=>i===0?ctx.moveTo(...p):ctx.lineTo(...p));ctx.closePath();}
 const rgba=(hex,alpha)=>{const v=hex.replace('#','');return `rgba(${parseInt(v.substring(0,2),16)},${parseInt(v.substring(2,4),16)},${parseInt(v.substring(4,6),16)},${alpha})`};
 function render(){
  ctx.clearRect(0,0,560,680);
  // Contact shadow, fixed to the white studio backdrop.
  const floor=ctx.createRadialGradient(285,587,15,285,587,175);
  floor.addColorStop(0,'rgba(39,89,113,.19)');floor.addColorStop(1,'rgba(39,89,113,0)');
  ctx.fillStyle=floor;ctx.save();ctx.translate(0,590);ctx.scale(1,.26);ctx.beginPath();ctx.arc(285,0,170,0,Math.PI*2);ctx.fill();ctx.restore();
  shellPath();const fill=ctx.createLinearGradient(175,200,390,530);
  fill.addColorStop(0,rgba(state.tint,.28));fill.addColorStop(.35,rgba(state.tint,.06));fill.addColorStop(.6,rgba(state.tint,.18));fill.addColorStop(1,rgba(state.tint,.45));ctx.fillStyle=fill;ctx.fill();
  ctx.lineWidth=3;ctx.strokeStyle='rgba(95,152,163,.28)';ctx.stroke();
  // Water surface and transparent lower body within silhouette.
  ctx.save();shellPath();ctx.clip();
  const water=ctx.createLinearGradient(190,340,372,550);
  water.addColorStop(0,'rgba(125,202,210,.23)');water.addColorStop(.44,'rgba(158,211,212,.15)');water.addColorStop(1,'rgba(91,161,181,.25)');
  ctx.beginPath();ctx.moveTo(177,354);ctx.lineTo(384,354);ctx.lineTo(358,555);ctx.lineTo(208,555);ctx.closePath();ctx.fillStyle=water;ctx.fill();
  ellipse(353);ctx.fillStyle='rgba(237,253,252,.35)';ctx.fill();ctx.strokeStyle='rgba(159,201,206,.65)';ctx.lineWidth=2;ctx.stroke();
  // Render moving highlights on curved glass from local azimuth, not a flat spin.
  for(const [theta,width,alpha] of [[-.96,12,.37],[-.66,4,.23],[.83,15,.29],[1.2,3,.2]]){
   const a=theta+state.yaw;
   if(Math.cos(a)<-.1)continue;
   const light=Math.max(0,Math.cos(a));
   ctx.beginPath();for(let j=0;j<=30;j++){const y=188+(539-188)*j/30;const p=proj(theta,y);j?ctx.lineTo(...p):ctx.moveTo(...p);}
   ctx.lineCap='round';ctx.lineWidth=width*(.5+light*.5);ctx.strokeStyle=`rgba(255,255,255,${alpha*light})`;ctx.stroke();
  }
  // Small rotating brand mark, projected onto the cylindrical surface.
  const markA=.25+state.yaw;
  if(Math.cos(markA)>0){
   const [mx,my]=proj(.25,320),vis=Math.cos(markA);
   ctx.save();ctx.translate(mx,my);ctx.transform(Math.max(.12,vis),0,0,1,0,0);
   ctx.fillStyle=`rgba(35,87,106,${.19+vis*.30})`;
   ctx.font='600 19px Trebuchet MS, Arial, sans-serif';ctx.textAlign='center';ctx.fillText('mul.',0,0);ctx.restore();
  }
  ctx.restore();
  // Base glass thickness and rim, two ellipses reinforce dimensionality.
  ellipse(551);ctx.strokeStyle='rgba(255,255,255,.61)';ctx.lineWidth=7;ctx.stroke();
  ellipse(551);ctx.strokeStyle='rgba(99,150,164,.25)';ctx.lineWidth=2;ctx.stroke();
  ellipse(180);ctx.fillStyle='rgba(243,253,253,.48)';ctx.fill();
  ellipse(180);ctx.strokeStyle='rgba(252,255,255,.98)';ctx.lineWidth=7;ctx.stroke();
  ellipse(180);ctx.strokeStyle='rgba(113,166,179,.5)';ctx.lineWidth=2;ctx.stroke();
  const rimShine=ctx.createLinearGradient(200,157,370,198);
  rimShine.addColorStop(0,'rgba(255,255,255,.42)');rimShine.addColorStop(.5,'rgba(255,255,255,.05)');rimShine.addColorStop(1,'rgba(255,255,255,.83)');
  ellipse(180);ctx.strokeStyle=rimShine;ctx.lineWidth=4;ctx.stroke();
 }
 function setAngle(delta){state.yaw+=delta;state.yaw=((state.yaw+Math.PI*10)%(Math.PI*2));render();$('rotate-reset').hidden=false;}
 canvas.addEventListener('pointerdown',e=>{if(e.button!==0)return;state.drag=true;state.x=e.clientX;state.y=e.clientY;state.moved=false;canvas.setPointerCapture(e.pointerId);stage.classList.add('is-dragging');});
 canvas.addEventListener('pointermove',e=>{if(!state.drag)return;const dx=e.clientX-state.x,dy=e.clientY-state.y;state.x=e.clientX;state.y=e.clientY;if(Math.abs(dx)>.15||Math.abs(dy)>.15){state.moved=true;state.pitch=Math.max(.12,Math.min(.43,state.pitch+dy*.002));setAngle(dx*.013);}});
 function endDrag(){if(!state.drag)return;state.drag=false;stage.classList.remove('is-dragging');if(state.moved)$('rotation-status').textContent='컵의 회전 각도를 변경했어요.';}
 canvas.addEventListener('pointerup',endDrag);canvas.addEventListener('pointercancel',endDrag);
 canvas.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();setAngle(e.key==='ArrowRight'?.18:-.18);$('rotation-status').textContent='컵의 회전 각도를 변경했어요.';}else if(e.key==='Home'){e.preventDefault();reset();}});
 function reset(){state.yaw=base;state.pitch=.23;$('rotate-reset').hidden=true;render();$('rotation-status').textContent='회전 각도를 초기화했어요.';}
 $('rotate-reset').addEventListener('click',reset);
 render();
 return {setTint:(tint,name)=>{state.tint=tint;state.name=name;canvas.setAttribute('aria-label',`${name} 컵 회전 보기. 좌우 방향키나 드래그로 회전할 수 있습니다.`);render();}};
}
