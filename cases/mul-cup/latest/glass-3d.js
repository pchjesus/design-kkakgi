/* MUL. E8 — procedural, hollow glass. Three.js r160.1 (MIT), local lazy dependency.
   Rendering is demand-driven; no idle animation loop or external models/textures. */
(()=>{
 'use strict';
 const host=document.querySelector('#colors .turn-control');
 const figure=host?.querySelector('.e6-cup-entrance');
 if(!host||!figure)return;
 const section=document.querySelector('#colors');
 const hint=host.querySelector('.drag-prompt');
 const reset=document.querySelector('#colors .reset-angle');
 let booting=false,renderer=null,scene=null,camera=null,model=null,envTarget=null;
 let visible=true,frame=0,resizeObserver=null,visibilityObserver=null,pointer=null,oldPoint=null;
 const mq=matchMedia('(prefers-reduced-motion: reduce)');
 const fallback=()=>{
  host.dataset.renderer='fallback';figure.classList.remove('mul-3d-ready');
  host.setAttribute('role','slider');host.setAttribute('aria-label','컵 좌우 회전');
  host.setAttribute('aria-valuemin','-85');host.setAttribute('aria-valuemax','85');host.setAttribute('aria-valuenow','0');
  hint.innerHTML='<span aria-hidden="true">↔</span> 기본 보기 · 좌우로 돌려보기';
 };
 const draw=()=>{frame=0;if(renderer&&visible&&!document.hidden)renderer.render(scene,camera);};
 const requestDraw=()=>{if(!frame&&renderer&&visible&&!document.hidden)frame=requestAnimationFrame(draw);};
 function syncAccessible(){
  host.removeAttribute('aria-valuemin');host.removeAttribute('aria-valuemax');host.removeAttribute('aria-valuenow');host.removeAttribute('aria-valuetext');
  if(model)host.dataset.orientation=model.quaternion.toArray().map(n=>n.toFixed(3)).join(',');
 }
 function restoreView(){
  if(!model)return;
  model.rotation.set(.12,-.28,0);syncAccessible();requestDraw();
 }
 function point(e){
  const r=host.getBoundingClientRect();
  const size=Math.min(r.width,r.height)*.62;
  const x=(e.clientX-r.left-r.width/2)/size,y=-(e.clientY-r.top-r.height*.44)/size;
  const d=x*x+y*y;
  return new THREE.Vector3(x,y,d<1?Math.sqrt(1-d):0).normalize();
 }
 function activate(){
  if(booting)return;booting=true;
  const loader=document.createElement('script');
  loader.src=new URL('vendor/three-0.160.1.min.js',document.baseURI).href;
  loader.onload=()=>{try{build();}catch(error){console.warn('MUL 3D fallback:',error.message);fallback();renderer?.dispose();}};
  loader.onerror=fallback;document.head.append(loader);
 }
 function build(){
  const T=THREE;
  renderer=new T.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});
  renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.6));
  renderer.outputColorSpace=T.SRGBColorSpace;renderer.toneMapping=T.ACESFilmicToneMapping;renderer.toneMappingExposure=1.15;
  renderer.setClearColor(0x000000,0);
  const canvas=renderer.domElement;canvas.className='glass-webgl';canvas.setAttribute('aria-hidden','true');
  scene=new T.Scene();camera=new T.PerspectiveCamera(35,1,.1,40);camera.position.set(0,.35,7.6);camera.lookAt(0,0,0);
  // Real studio geometry produces reflections, without fetching an HDR photograph.
  const room=new T.Scene();room.background=new T.Color('#c9dde8');
  room.add(new T.Mesh(new T.BoxGeometry(12,10,12),new T.MeshBasicMaterial({color:'#b9d0df',side:T.BackSide})));
  function softbox(x,y,z,w,h,color,intensity){const p=new T.Mesh(new T.PlaneGeometry(w,h),new T.MeshBasicMaterial({color:new T.Color(color).multiplyScalar(intensity),side:T.DoubleSide}));p.position.set(x,y,z);p.lookAt(0,0,0);room.add(p);}
  softbox(-3,1,3,1.3,5,'#ffffff',3.2);softbox(3,1,1,1,4,'#e2f3ff',2.2);softbox(0,4,0,5,3,'#ffffff',2);softbox(0,0,-4,4,5,'#66879e',.6);
  const pmrem=new T.PMREMGenerator(renderer);envTarget=pmrem.fromScene(room,.08);scene.environment=envTarget.texture;pmrem.dispose();
  room.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
  scene.add(new T.HemisphereLight(0xf5fbff,0x56798e,2));
  const key=new T.DirectionalLight(0xffffff,2.8);key.position.set(-3,5,4);scene.add(key);
  model=new T.Group();scene.add(model);
  const glass=new T.MeshPhysicalMaterial({color:'#effaff',metalness:0,roughness:.095,transmission:.97,thickness:.12,ior:1.47,clearcoat:1,clearcoatRoughness:.055,envMapIntensity:.95,attenuationColor:new T.Color('#d2edf1'),attenuationDistance:2.7,side:T.DoubleSide});
  // Revolved closed profile: outer wall -> rounded lip -> inner wall -> thick bottom.
  const profile=[[0,-1.45],[.65,-1.45],[.77,-1.43],[.83,-1.34],[.91,-.9],[.98,-.1],[.97,.7],[.935,1.36],[.93,1.43],[.91,1.45],[.887,1.43],[.884,1.36],[.92,.7],[.925,-.1],[.85,-.9],[.78,-1.21],[.66,-1.27],[0,-1.27]];
  const curve=new T.CatmullRomCurve3(profile.map(([x,y])=>new T.Vector3(x,y,0)),false,'centripetal');
  const points=curve.getPoints(90).map(v=>new T.Vector2(Math.max(0,v.x),v.y));
  const shell=new T.Mesh(new T.LatheGeometry(points,112),glass);shell.name='hollow-glass';model.add(shell);
  const rim=new T.Mesh(new T.TorusGeometry(.909,.014,10,112),glass);rim.rotation.x=Math.PI/2;rim.position.y=1.435;model.add(rim);
  const foot=new T.Mesh(new T.TorusGeometry(.725,.034,12,96),glass);foot.rotation.x=Math.PI/2;foot.position.y=-1.395;model.add(foot);
  const waterMaterial=new T.MeshPhysicalMaterial({color:'#d5edf1',metalness:0,roughness:.055,transmission:.95,thickness:.65,ior:1.333,envMapIntensity:.55,attenuationColor:new T.Color('#9acfd9'),attenuationDistance:3,side:T.DoubleSide});
  const waterProfile=[[0,-1.25],[.65,-1.25],[.77,-1.19],[.84,-.9],[.925,.03],[.923,.09],[0,.09]].map(([x,y])=>new T.Vector2(x,y));
  const water=new T.Mesh(new T.LatheGeometry(waterProfile,96),waterMaterial);water.name='water-volume';model.add(water);
  const meniscus=new T.Mesh(new T.TorusGeometry(.914,.009,8,96),waterMaterial);meniscus.rotation.x=Math.PI/2;meniscus.position.y=.09;model.add(meniscus);
  const labelCanvas=document.createElement('canvas');labelCanvas.width=512;labelCanvas.height=256;
  const ctx=labelCanvas.getContext('2d');ctx.strokeStyle='#386377';ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(256,20);ctx.bezierCurveTo(210,83,207,111,256,112);ctx.bezierCurveTo(305,111,302,83,256,20);ctx.stroke();ctx.fillStyle='#386377';ctx.font='38px sans-serif';ctx.textAlign='center';ctx.fillText('M U L.',256,188);
  const labelTexture=new T.CanvasTexture(labelCanvas);labelTexture.colorSpace=T.SRGBColorSpace;
  const label=new T.Mesh(new T.CylinderGeometry(.987,.987,.38,48,1,true,-.28,.56),new T.MeshBasicMaterial({map:labelTexture,transparent:true,opacity:.72,depthWrite:false,side:T.DoubleSide}));label.position.y=.63;model.add(label);
  function color(){
   const name=document.querySelector('#colors .swatch.selected')?.dataset.color||'clear';
   const values={clear:['#effaff','#c7e8ef',2.7],amber:['#d9b07c','#a66b34',1.3],smoke:['#b2c2ce','#6e859a',1.8]}[name];
   glass.color.set(values[0]);glass.attenuationColor.set(values[1]);glass.attenuationDistance=values[2];host.dataset.color=name;requestDraw();
  }
  // Observe the existing selection state so drawer and stage remain one contract.
  const colorObserver=new MutationObserver(color);colorObserver.observe(document.querySelector('#colors .swatches'),{subtree:true,attributes:true,attributeFilter:['aria-pressed']});
  figure.append(canvas);figure.classList.add('mul-3d-ready');host.dataset.renderer='three';host.setAttribute('role','group');host.setAttribute('aria-label','컵 3차원 보기');host.setAttribute('aria-describedby','glass-control-hint');host.setAttribute('aria-keyshortcuts','ArrowUp ArrowDown ArrowLeft ArrowRight Home');
  hint.innerHTML='<span class="orbit-symbol" aria-hidden="true">⤢</span> 드래그로 자유롭게 돌려보세요';
  host.title='드래그: 자유 회전 · 방향키: 상하좌우 회전 · Home: 처음 각도';
  reset.textContent='처음 각도로';
  host.addEventListener('pointerdown',e=>{if(e.pointerType==='mouse'&&e.button!==0)return;e.stopImmediatePropagation();pointer=e.pointerId;oldPoint=point(e);host.setPointerCapture(pointer);host.classList.add('is-rotating');},{capture:true});
  host.addEventListener('pointermove',e=>{if(pointer!==e.pointerId||!oldPoint)return;e.stopImmediatePropagation();const next=point(e);const q=new T.Quaternion().setFromUnitVectors(oldPoint,next);model.quaternion.premultiply(q).normalize();oldPoint=next;syncAccessible();requestDraw();},{capture:true});
  const release=e=>{if(pointer!==e.pointerId)return;e.stopImmediatePropagation();pointer=null;oldPoint=null;host.classList.remove('is-rotating');};
  host.addEventListener('pointerup',release,{capture:true});host.addEventListener('pointercancel',release,{capture:true});host.addEventListener('lostpointercapture',()=>{pointer=null;oldPoint=null;host.classList.remove('is-rotating');});
  host.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home'].includes(e.key))return;e.preventDefault();e.stopImmediatePropagation();if(e.key==='Home'){restoreView();return;}const axis=e.key==='ArrowLeft'||e.key==='ArrowRight'?new T.Vector3(0,1,0):new T.Vector3(1,0,0);const sign=e.key==='ArrowRight'||e.key==='ArrowDown'?1:-1;model.quaternion.premultiply(new T.Quaternion().setFromAxisAngle(axis,sign*Math.PI/18));syncAccessible();requestDraw();},{capture:true});
  host.addEventListener('dblclick',restoreView);reset.addEventListener('click',restoreView);
  const size=()=>{const r=figure.getBoundingClientRect();const w=figure.clientWidth,h=figure.clientHeight;if(!w||!h)return;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();requestDraw();};
  resizeObserver=new ResizeObserver(size);resizeObserver.observe(figure);
  visibilityObserver=new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(visible)requestDraw();});visibilityObserver.observe(host);
  document.addEventListener('visibilitychange',requestDraw);
  canvas.addEventListener('webglcontextlost',e=>{e.preventDefault();fallback();canvas.remove();},{once:true});
  restoreView();color();size();
  window.addEventListener('pagehide',e=>{if(e.persisted)return;resizeObserver.disconnect();visibilityObserver.disconnect();colorObserver.disconnect();if(frame)cancelAnimationFrame(frame);scene.traverse(o=>{o.geometry?.dispose();if(o.material){o.material.map?.dispose();o.material.dispose();}});envTarget.dispose();renderer.dispose();},{once:true});
 }
 if('IntersectionObserver' in window){const lazy=new IntersectionObserver(entries=>{if(entries.some(e=>e.isIntersecting)){lazy.disconnect();activate();}},{rootMargin:'650px'});lazy.observe(host);}else activate();
})();
