(this.webpackJsonpuntitled=this.webpackJsonpuntitled||[]).push([[0],{10:function(e,t,a){e.exports={notification:"Notification_notification__2fMW3",notificationContent:"Notification_notificationContent__3U5_2",notificationUser:"Notification_notificationUser__1wsPX",notificationText:"Notification_notificationText__3KTF0",notificationClose:"Notification_notificationClose__kOyTA"}},15:function(e,t,a){e.exports={container:"UserList_container__2_-sc",searchContainer:"UserList_searchContainer__NeQ3E",search:"UserList_search__2jubq"}},17:function(e,t,a){e.exports={app:"App_app__2WJfA","App-logo":"App_App-logo__27M-q",appLogo:"App_appLogo__5BAM9","App-logo-spin":"App_App-logo-spin__38JR9",transparentSnackbar:"App_transparentSnackbar__2Znso"}},18:function(e,t,a){e.exports={toggleContainer:"ThemeToggle_toggleContainer__1GEhY",toggleSlider:"ThemeToggle_toggleSlider__Q-xG7"}},20:function(e,t,a){e.exports={scrollButton:"ScrollDown_scrollButton__3REEp",scrollButtonHide:"ScrollDown_scrollButtonHide__HiKNF"}},29:function(e,t,a){e.exports=a(51)},3:function(e,t,a){e.exports={message:"Message_message__2_RMz",leftMessage:"Message_leftMessage__1VfeK",rightMessage:"Message_rightMessage__Fh45H",fileAttachment:"Message_fileAttachment__3sbql",file:"Message_file__tF3TQ",fileName:"Message_fileName__TuoP9",image:"Message_image__2I5c8",video:"Message_video__1BKkF",document:"Message_document__1Fhpc",fileSize:"Message_fileSize__285Nr",messageText:"Message_messageText__2dnAL",messageInfo:"Message_messageInfo__2x5Az",statusError:"Message_statusError__3q3bB",statusSent:"Message_statusSent__LlSH_",statusSending:"Message_statusSending__yGdxr",dateTime:"Message_dateTime__3JMQA",shimmerSquare:"Message_shimmerSquare__3i__N",shimmer:"Message_shimmer__1Aker"}},35:function(e,t,a){},4:function(e,t,a){e.exports={mainWindow:"Messenger_mainWindow__IZIYJ",container:"Messenger_container__JzgK_",header:"Messenger_header__wMfMB",burgerMenu:"Messenger_burgerMenu__3Xuj2",burgerLine:"Messenger_burgerLine__3qUFP",connectionStatus:"Messenger_connectionStatus__2hK2T",infoContainer:"Messenger_infoContainer__159Vt",userFullName:"Messenger_userFullName__1QaTm",chatId:"Messenger_chatId__2NI1y",content:"Messenger_content__3m4wu",messages:"Messenger_messages__13xEj",dateSeparator:"Messenger_dateSeparator__19WYA",dateSeparatorText:"Messenger_dateSeparatorText__9AZLa"}},5:function(e,t,a){e.exports={connectingContainer:"Chat_connectingContainer__8vB8A",connecting:"Chat_connecting__clgPY",connectingDot:"Chat_connectingDot__3ZhMt",blink:"Chat_blink__2xmqZ",serverIcon:"Chat_serverIcon__2yIW5",pulse:"Chat_pulse__1TsKF",connectingArrows:"Chat_connectingArrows__2SMIa",connectingArrow:"Chat_connectingArrow__2jrl7",chatContainer:"Chat_chatContainer__1hQZN",userList:"Chat_userList__2BEJI",visible:"Chat_visible__5605_",chat:"Chat_chat__R0dBl"}},51:function(e,t,a){"use strict";a.r(t);var s=a(0),n=a.n(s),i=a(27),r=a.n(i),o=(a(35),a(17)),l=a.n(o),c=a(7),m=a.n(c);var d=e=>{let{className:t}=e;return n.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 32 32"},n.a.createElement("title",null,"About"),n.a.createElement("g",{id:"about",className:t},n.a.createElement("path",{d:"M16,16A7,7,0,1,0,9,9,7,7,0,0,0,16,16ZM16,4a5,5,0,1,1-5,5A5,5,0,0,1,16,4Z"}),n.a.createElement("path",{d:"M17,18H15A11,11,0,0,0,4,29a1,1,0,0,0,1,1H27a1,1,0,0,0,1-1A11,11,0,0,0,17,18ZM6.06,28A9,9,0,0,1,15,20h2a9,9,0,0,1,8.94,8Z"})))};var u=e=>{let{user:t,onSelectUser:a,unreadCount:s}=e;return n.a.createElement("div",{className:m.a.userCard,onClick:()=>a(t)},n.a.createElement("div",{className:m.a.userInfoContainer},n.a.createElement("div",{className:m.a.userIconContainer},n.a.createElement(d,{className:m.a.userIcon})),n.a.createElement("div",{className:m.a.userInfo},n.a.createElement("div",{className:m.a.userFullName},t.name," ",t.surname),n.a.createElement("div",{className:m.a.additionInfo},t.phone))),s>0&&n.a.createElement("div",{className:m.a.unreadCount},n.a.createElement("div",{className:m.a.count},s)))},_=a(15),g=a.n(_),p=a(18),f=a.n(p);var h=()=>{const[e,t]=Object(s.useState)(!1);Object(s.useEffect)(()=>{const e=localStorage.getItem("theme");e&&(t("dark"===e),document.documentElement.setAttribute("data-theme",e))},[]);return n.a.createElement("label",{className:f.a.toggleContainer},n.a.createElement("input",{type:"checkbox",checked:e,onChange:()=>{const a=e?"light":"dark";document.documentElement.setAttribute("data-theme",a),t(!e),localStorage.setItem("theme",a)}}),n.a.createElement("span",{className:f.a.toggleSlider}))};var E=e=>{let{users:t,onSelectUser:a,unreadCounts:i}=e;const[r,o]=Object(s.useState)(""),l=t.filter(e=>e.name.toLowerCase().includes(r.toLowerCase())||e.surname.toLowerCase().includes(r.toLowerCase()));return n.a.createElement("div",{className:g.a.container},n.a.createElement("div",{className:g.a.searchContainer},n.a.createElement("div",{style:{width:"60px"}}),n.a.createElement("input",{className:g.a.search,type:"text",placeholder:"\u041f\u043e\u0438\u0441\u043a...",value:r,onChange:e=>o(e.target.value)}),n.a.createElement(h,null)),n.a.createElement("div",null,l.map(e=>n.a.createElement(u,{key:e.id,user:e,onSelectUser:a,unreadCount:i[e.id]||0}))))},v=a(53);const N=window.env.FAST_API_URL,C=window.env.API_KEY,w=N+"/api",y="https://api.telegram.org/bot"+C,M="https://api.telegram.org/file/bot"+C,S=v.a.create({baseURL:w,headers:{Authorization:"Bearer "+C}}),b=async function(e,t){let a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";const s=y+"/sendPhoto",n=new FormData;n.append("chat_id",e),n.append("photo",t),a&&n.append("caption",a);const i=await v.a.post(s,n,{headers:{"Content-Type":"multipart/form-data"}}),r=i.data.result.photo[i.data.result.photo.length-1],o=r.file_id,l=r.file_size;return i.data.result.document={file_name:t.name,file_id:o,file_size:l,mime_type:t.type},i.data.result},I=async function(e,t){let a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";const s=y+"/sendVideo",n=new FormData;n.append("chat_id",e),n.append("video",t),a&&n.append("caption",a);const i=await v.a.post(s,n,{headers:{"Content-Type":"multipart/form-data"}}),r=i.data.result.video,o=r.file_id,l=r.file_size;return i.data.result.document={file_name:t.name,file_id:o,file_size:l,mime_type:t.type},console.log(i.data.result),i.data.result},x=async function(e,t){let a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";const s=y+"/sendDocument",n=new FormData;n.append("chat_id",e),n.append("document",t),a&&n.append("caption",a);const i=await v.a.post(s,n,{headers:{"Content-Type":"multipart/form-data"}});return i.data.result};var k=a(6),A=a.n(k);var O=e=>{let{color:t,width:a,height:s,style:i,strokeWidth:r=1.5}=e;return n.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"icon icon-tabler icon-tabler-paperclip",fill:"none",height:s,stroke:t,strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:r,viewBox:"0 0 24 24",width:a,style:i},n.a.createElement("path",{d:"M0 0h24v24H0z",fill:"none",stroke:"none"}),n.a.createElement("path",{d:"M15 7l-6.5 6.5a1.5 1.5 0 0 0 3 3l6.5 -6.5a3 3 0 0 0 -6 -6l-6.5 6.5a4.5 4.5 0 0 0 9 9l6.5 -6.5"}))};var F=e=>{let{color:t,width:a,height:s,style:i}=e;return n.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",xmlnsXlink:"http://www.w3.org/1999/xlink",width:a,height:s,viewBox:"0 0 20 18",style:i},n.a.createElement("title",null,"send"),n.a.createElement("desc",null,"Created with Sketch."),n.a.createElement("g",{id:"Icons",stroke:"none",strokeWidth:"1",fill:"none",fillRule:"evenodd"},n.a.createElement("g",{id:"Rounded",transform:"translate(-374.000000, -1529.000000)"},n.a.createElement("g",{id:"Content",transform:"translate(100.000000, 1428.000000)"},n.a.createElement("g",{id:"-Round-/-Content-/-send",transform:"translate(272.000000, 98.000000)"},n.a.createElement("g",null,n.a.createElement("polygon",{id:"Path",points:"0 0 24 0 24 24 0 24"}),n.a.createElement("path",{d:"M3.4,20.4 L20.85,12.92 C21.66,12.57 21.66,11.43 20.85,11.08 L3.4,3.6 C2.74,3.31 2.01,3.8 2.01,4.51 L2,9.12 C2,9.62 2.37,10.05 2.87,10.11 L17,12 L2.87,13.88 C2.37,13.95 2,14.38 2,14.88 L2.01,19.49 C2.01,20.2 2.74,20.69 3.4,20.4 Z",id:"\ud83d\udd39Icon-Color",fill:t})))))))};var j=e=>{let{userId:t,onSendMessage:a,socket:i}=e;const[r,o]=Object(s.useState)(""),[l,c]=Object(s.useState)([]),m=Object(s.useRef)(null),d=Object(s.useRef)(null),u=Object(s.useRef)(1);Object(s.useEffect)(()=>{const{message:e,files:a}=p(t);o(e),c(a),console.log(a)},[t]),Object(s.useEffect)(()=>{_()},[r]);const _=()=>{const e=m.current;e&&(e.style.height="34px",e.style.height=e.scrollHeight+"px")},g=(e,t,a)=>{sessionStorage.setItem("message_"+e,t);const s=a.map(e=>({name:e.name,lastModified:e.lastModified,size:e.size,type:e.type}));sessionStorage.setItem("files_"+e,JSON.stringify(s))},p=e=>{const t=sessionStorage.getItem("message_"+e),a=sessionStorage.getItem("files_"+e);return{message:t||"",files:(a?JSON.parse(a):[]).map(e=>new File([],e.name,{lastModified:e.lastModified,size:e.size,type:e.type}))}};return n.a.createElement("div",{className:A.a.inputContainer},l.length>0&&n.a.createElement("div",{className:A.a.attachedFiles},l.map((e,a)=>n.a.createElement("div",{key:a,className:A.a.attachedFileContainer},n.a.createElement("div",{className:A.a.attachedFileCounterWeight}),n.a.createElement("div",{className:A.a.attachedFile},e.name),n.a.createElement("div",{className:A.a.attachedFileCancel,onClick:()=>(e=>{c(t=>{const a=[...t];return a.splice(e,1),a}),g(t,r,l.filter((t,a)=>a!==e))})(a)},n.a.createElement("div",{className:A.a.attachedFileCancelLine}),n.a.createElement("div",{className:A.a.attachedFileCancelLine}))))),n.a.createElement("div",{style:{display:"flex",justifyContent:"space-around",width:"100%",alignItems:"flex-end"}},n.a.createElement("div",{className:A.a.AttachButton,style:{margin:"0 8px 0 8px",display:"flex",justifyItems:"center",alignItems:"center"},onClick:()=>d.current.click()},"dark"===localStorage.getItem("theme")?n.a.createElement(O,{color:"#8673e0",width:"32px",height:"32px"}):n.a.createElement(O,{color:"#338feb",width:"32px",height:"32px"})),n.a.createElement("textarea",{ref:m,className:A.a.TextArea,placeholder:"\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435...",value:r,onChange:e=>{const a=e.target.value;o(a),g(t,a,l)},onInput:_}),n.a.createElement("input",{type:"file",multiple:!0,onChange:e=>{const a=Array.from(e.target.files);c(e=>[...e,...a]),g(t,r,[...l,...a])},className:A.a.fileInput,style:{display:"none"},ref:d}),n.a.createElement("div",{className:A.a.sendButtonContainer,style:{margin:"0 8px 0 8px",display:"flex",justifyItems:"center",alignItems:"center"},onClick:async()=>{if(r.trim()||l.length>0){const s=u.current++,n={id:s,text:r,status:"sending",sender:0,recipient:t,date:Date.now()/1e3,files:[],old_id:null};if(l.length>0){const e={...n,files_count:l.length};a(e)}else a(n);delete n.files_count,o(""),c([]),g(t,"",[]);try{if(l.length>0){let e;if(1===l.length){const o=await async function(e,t){let a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";const s=t.type;return s.startsWith("image/")?b(e,t,a):s.startsWith("video/")?I(e,t,a):x(e,t,a)}(t,l[0],r);e=[{file:l[0],response:o.document}];const c={...n,status:"sent",id:o.message_id,date:o.date,files:e.map(e=>({file_name:e.response.file_name,file_id:e.response.file_id,file_size:e.response.file_size,mime_type:e.response.mime_type}))};a({...c,old_id:s}),delete c.old_id,i.emit("updateMessage",{user:c.recipient,message:c})}else{const o=await async function(e,t){let a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";const s=new FormData;s.append("chat_id",e);const n=t.map((e,t)=>{const n=e.type.startsWith("image/")?"photo":e.type.startsWith("video/")?"video":"document",i="random-name-"+t;return s.append(i,e),{type:n,media:"attach://"+i,caption:0===t?a:"",parse_mode:"HTML"}});s.append("media",JSON.stringify(n));const i=await v.a.post(y+"/sendMediaGroup",s,{headers:{"Content-Type":"multipart/form-data"}});return i.data.result.forEach((e,a)=>{const s=e.photo?e.photo[e.photo.length-1]:e.video?e.video:e.document,n=s.file_id,i=s.file_size;e.document={file_name:t[a].name,file_id:n,file_size:i,mime_type:t[a].type}}),console.log(i.data.result),i.data.result}(t,l,r);e=o.map((e,t)=>({file:l[t],response:e.document||e.photo||e.video}));const c={...n,status:"sent",id:o[0].message_id,date:o[0].date,files:e.map(e=>({file_name:e.response.file_name,file_id:e.response.file_id,file_size:e.response.file_size,mime_type:e.response.mime_type}))};a({...c,old_id:s}),delete c.old_id,i.emit("updateMessage",{user:c.recipient,message:c})}}else{const e=await(async(e,t)=>(await v.a.post(y+"/sendMessage",{chat_id:e,text:t})).data.result)(t,r),o={...n,status:"sent",id:e.message_id,date:e.date};a({...o,old_id:s}),delete o.old_id,i.emit("updateMessage",{user:o.recipient,message:o})}}catch(e){a({...n,status:"error",date:Date.now()/1e3,old_id:s})}}}},"dark"===localStorage.getItem("theme")?n.a.createElement(F,{color:"#8673e0",width:"32px",height:"32px"}):n.a.createElement(F,{color:"#338feb",width:"32px",height:"32px"}))))},L=a(3),B=a.n(L),T=a(19),z=a.n(T);z.a.setAppElement("#root");var D=e=>{let{message:t}=e;const[a,i]=Object(s.useState)(!0),[r,o]=Object(s.useState)([]),[l,c]=Object(s.useState)(!1),[m,d]=Object(s.useState)(""),u=0===t.sender?B.a.rightMessage:B.a.leftMessage;Object(s.useEffect)(()=>{const e=async()=>{const e=await Promise.all(t.files.map(async e=>{if(e.mime_type&&e.mime_type.startsWith("image/")&&e.file_size>5242880)return{name:e.file_name,size:e.file_size,mime_type:e.mime_type,file_is_too_big:!0};if(e.mime_type&&e.file_size>20971520)return{name:e.file_name,size:e.file_size,mime_type:e.mime_type,file_is_too_big:!0};const t=await(async e=>{const t=y+"/getFile",a=await v.a.post(t,{file_id:e});return`${M}/${a.data.result.file_path}`})(e.file_id);return{name:e.file_name,size:e.file_size,url:t,mime_type:e.mime_type,file_is_too_big:!1}}));o(e),i(!1)};t.files.length>0&&e()},[t.files]);const _=e=>{if(0===e)return"0 Bytes";const t=Math.floor(Math.log(e)/Math.log(1024));return parseFloat((e/Math.pow(1024,t)).toFixed(2))+" "+["Bytes","KB","MB","GB","TB"][t]};return n.a.createElement("div",{className:`${B.a.message} ${u}`},t.files_count>0&&n.a.createElement("div",{className:B.a.fileAttachment},Array.from({length:t.files_count}).map((e,t)=>n.a.createElement("div",{className:B.a.shimmerSquare,key:t}))),t.files.length>0&&a?n.a.createElement("div",{className:B.a.fileAttachment},Array.from({length:t.files.length}).map((e,t)=>n.a.createElement("div",{className:B.a.shimmerSquare,key:t}))):r.length>0?n.a.createElement("div",{className:B.a.fileAttachment},r.map((e,t)=>n.a.createElement("div",{className:B.a.file,key:t},e.mime_type&&e.mime_type.startsWith("image/")&&!e.file_is_too_big?n.a.createElement("div",{onClick:()=>{return t=e.url,d(t),void c(!0);var t},style:{cursor:"pointer"}},n.a.createElement("img",{className:B.a.image,src:e.url,alt:e.name})):e.mime_type&&e.mime_type.startsWith("video/")&&!e.file_is_too_big?n.a.createElement("a",{href:e.url,download:e.name},n.a.createElement("video",{className:B.a.video,src:e.url,alt:e.name,controls:!0})):e.mime_type&&e.file_is_too_big?n.a.createElement("div",{className:B.a.document},n.a.createElement("div",null,"\u0424\u0430\u0439\u043b \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u0435\u043d"),n.a.createElement("div",{className:B.a.fileName},e.name),n.a.createElement("div",{className:B.a.fileSize},_(e.size))):n.a.createElement("a",{href:e.url,download:e.name},n.a.createElement("div",{className:B.a.document},n.a.createElement("div",null,"\u0424\u0410\u0419\u041b"),n.a.createElement("div",{className:B.a.fileName},e.name),n.a.createElement("div",{className:B.a.fileSize},_(e.size))))))):null,n.a.createElement("div",{className:B.a.messageText},t.text),n.a.createElement("div",{className:B.a.messageInfo},n.a.createElement("span",{className:B.a.dateTime},(e=>{const t=new Date(1e3*e);return`${t.getHours().toString().padStart(2,"0")}:${t.getMinutes().toString().padStart(2,"0")}`})(t.date)),0===t.sender&&n.a.createElement(n.a.Fragment,null,"sending"===t.status&&n.a.createElement("span",{className:B.a.statusSending},n.a.createElement("div",{className:B.a.status},"\u25f4")),"sent"===t.status&&n.a.createElement("span",{className:B.a.statusSent},"\u2713"),"error"===t.status&&n.a.createElement("span",{className:B.a.statusError},"\u2716"))),n.a.createElement(z.a,{isOpen:l,onRequestClose:()=>{c(!1)},contentLabel:"Image Modal",style:{content:{maxWidth:"80%",maxHeight:"80%",margin:"auto"}}},n.a.createElement("img",{src:m,alt:"Full size",style:{width:"100%",height:"auto"}})))},U=a(4),R=a.n(U);var W=e=>{const t=new Date,a=new Date(1e3*e),s=t.toDateString()===a.toDateString(),n=new Date(t.setDate(t.getDate()-1)).toDateString()===a.toDateString();if(s)return"\u0421\u0435\u0433\u043e\u0434\u043d\u044f";if(n)return"\u0412\u0447\u0435\u0440\u0430";{const e={day:"numeric",month:"long"};return a.toLocaleDateString("ru-RU",e)}},J=a(20),H=a.n(J);var Z=function(e){let{showScrollButton:t,onClick:a}=e;return n.a.createElement("div",{className:t?H.a.scrollButton:H.a.scrollButtonHide,onClick:a},"\u2193")};var P=e=>{let{user:t,toggleUserList:a,newMessages:i,addedMessagesRef:r,socket:o}=e;const[l,c]=Object(s.useState)([]),[m,d]=Object(s.useState)(!1),u=Object(s.useRef)(null),_=Object(s.useRef)(null);Object(s.useEffect)(()=>{if(t){(async()=>{const e=JSON.parse(sessionStorage.getItem("messages_"+t.id)||"[]"),a=JSON.parse(sessionStorage.getItem("unreadMessages_"+t.id)||"[]");let s=[...e,...a];if(!(t.id in r.current)){const e=await(async e=>(await S.get("/messages/"+e)).data.messages)(t.id);s=[...e,...s],r.current[t.id]=!0,console.log("old",e)}const n=Array.from(new Set(s.map(e=>e.id))).map(e=>s.find(t=>t.id===e));c(n),console.log("stored",e),console.log("new messages",a),console.log("combined",n),await(async e=>{await S.post("/markMessagesAsRead/"+e)})(t.id),sessionStorage.setItem("messages_"+t.id,JSON.stringify(n)),sessionStorage.removeItem("unreadMessages_"+t.id),console.log("combined was saved on storage",sessionStorage.getItem("messages_"+t.id)),console.log("new messages was deleted",sessionStorage.getItem("unreadMessages_"+t.id))})()}},[t,r]),Object(s.useEffect)(()=>{setTimeout(()=>{g({behavior:"instant"})},0)},[l]),Object(s.useEffect)(()=>{t&&i&&i[t.id]&&(console.log("for user ",t.id," message was handled"),c(e=>{const a=[...e];return i[t.id].forEach(t=>{e.some(e=>e.id===t.id)||a.push(t)}),console.log("for user ",t.id," messages was updated: ",a),a}))},[i,t,r]);const g=e=>{var t;null===(t=u.current)||void 0===t||t.scrollIntoView(e)};return Object(s.useEffect)(()=>{const e=new IntersectionObserver(e=>{let[t]=e;d(!t.isIntersecting)},{root:_.current,rootMargin:"0px 0px 2000px 0px",threshold:.1}),t=u.current;return t&&e.observe(t),()=>{t&&e.unobserve(t)}},[l]),n.a.createElement("div",{className:R.a.mainWindow},n.a.createElement("div",{className:R.a.container},n.a.createElement("div",{className:R.a.header},n.a.createElement("div",{className:R.a.connectionStatus,onClick:a},n.a.createElement("div",{className:R.a.burgerMenu},n.a.createElement("div",{className:R.a.burgerLine}),n.a.createElement("div",{className:R.a.burgerLine}),n.a.createElement("div",{className:R.a.burgerLine}))),n.a.createElement("div",{className:R.a.infoContainer},n.a.createElement("div",{className:R.a.userFullName},t.name," ",t.surname),n.a.createElement("div",{className:R.a.chatId},t.id)),n.a.createElement("div",{className:R.a.burgerMenu})),n.a.createElement("div",{className:R.a.content},n.a.createElement("div",{className:R.a.messages,ref:_},l.slice().sort((e,t)=>e.date-t.date).map((e,t)=>{const a=new Date(1e3*e.date),s=l[t-1],i=s?new Date(1e3*s.date):null,r=!i||a.toDateString()!==i.toDateString();return n.a.createElement(n.a.Fragment,{key:e.id},r&&n.a.createElement("div",{className:R.a.dateSeparator},n.a.createElement("span",{className:R.a.dateSeparatorText},W(e.date))),n.a.createElement(D,{message:e}))}),n.a.createElement("div",{ref:u}," ")),n.a.createElement(Z,{showScrollButton:m,onClick:()=>g({behavior:"smooth"})})),n.a.createElement(j,{userId:t.id,onSendMessage:e=>{c(a=>{const s=null===e.old_id?[...a,e]:a.map(t=>t.id===e.old_id?e:t);return sessionStorage.setItem("messages_"+t.id,JSON.stringify(s)),s})},socket:o})))},q=a(5),K=a.n(q),Q=a(9),$=a(10),G=a.n($);var Y=e=>{let{user:t,message:a,onClickOpen:s,onClickOk:i}=e;return n.a.createElement("div",{className:G.a.notification},n.a.createElement("div",{onClick:s,className:G.a.notificationContent},n.a.createElement("div",{className:G.a.notificationUser},t.name," ",t.surname),n.a.createElement("div",{className:G.a.notificationText},a)),n.a.createElement("div",{onClick:i,className:G.a.notificationClose},"\u041e\u043a"))},V=a(28);const X=window.env.FAST_API_URL;var ee=Object(V.a)(X,{transports:["websocket"],withCredentials:!0,extraHeaders:{"my-custom-header":"abcd"}});var te=()=>{const[e,t]=Object(s.useState)(null),[a,i]=Object(s.useState)([]),[r,o]=Object(s.useState)(!0),[l,c]=Object(s.useState)({}),[m,d]=Object(s.useState)({}),u=Object(s.useRef)({}),[_,g]=Object(s.useState)(!1),p=e=>{t(e),o(!1),c(t=>({...t,[e.id]:0}))},f=Object(s.useCallback)(t=>{if(console.log("New message received:",t),0!==t.message.sender){c(e=>({...e,[t.user]:(e[t.user]||0)+1}));const s=a.find(e=>e.id===t.user);s!==e&&Object(Q.c)(n.a.createElement(Y,{user:s,message:t.message.text,onClickOpen:()=>{const e=a.find(e=>e.id===t.user);e&&(p(e),Object(Q.b)())},onClickOk:()=>Object(Q.b)()}))}else c(e=>({...e,[t.user]:0}));d(e=>{const a=e[t.user]||[];if(!a.some(e=>e.id===t.message.id)){const s={...e,[t.user]:[...a,t.message]};let n=JSON.parse(sessionStorage.getItem("unreadMessages_"+t.user)||"[]");return Array.isArray(n)||(n=[]),n.push(t.message),sessionStorage.setItem("unreadMessages_"+t.user,JSON.stringify(n)),s}return console.log("Contain:",m),e})},[m,a,e]);return Object(s.useEffect)(()=>(ee.on("newMessage",f),()=>{ee.off("newMessage",f)}),[f]),Object(s.useEffect)(()=>(ee.on("connect",()=>{g(!0)}),ee.on("disconnect",()=>{g(!1)}),()=>{ee.off("connect"),ee.off("disconnect")}),[]),Object(s.useEffect)(()=>{(async()=>{try{const e=(await(async()=>(await S.get("/unreadMessages")).data.unread_messages)()).reduce((e,t)=>{const a=t.user;return e[a]||(e[a]={messages:[],count:0}),e[a].messages.push(t.message),e[a].count+=1,e},{});Object.keys(e).forEach(t=>{const{messages:a,count:s}=e[t];sessionStorage.setItem("unreadMessages_"+t,JSON.stringify(a)),c(e=>({...e,[t]:s}))})}catch(e){console.error("Error fetching unread messages:",e)}})()},[]),Object(s.useEffect)(()=>{(async()=>{const e=await(async()=>(await S.get("/users")).data.users)();i(e)})()},[]),_?n.a.createElement("div",{className:K.a.chatContainer},n.a.createElement("div",{className:`${K.a.userList} ${r?K.a.visible:""}`},n.a.createElement(E,{users:a,onSelectUser:p,unreadCounts:l})),n.a.createElement("div",{className:K.a.chat},e?n.a.createElement(P,{user:e,toggleUserList:()=>{r||(c(t=>({...t,[e.id]:0})),t(null)),o(!r)},newMessages:m,addedMessagesRef:u,socket:ee}):n.a.createElement("p",null,"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u0447\u0442\u043e\u0431\u044b \u043d\u0430\u0447\u0430\u0442\u044c \u043e\u0431\u0449\u0435\u043d\u0438\u0435."))):n.a.createElement("div",{className:K.a.connectingContainer},n.a.createElement("div",{className:K.a.connecting},n.a.createElement("div",{className:K.a.serverIcon}),n.a.createElement("div",{className:K.a.connectingArrows},n.a.createElement("div",{className:K.a.connectingArrow}),n.a.createElement("div",{className:K.a.connectingArrow}),n.a.createElement("div",{className:K.a.connectingArrow}))),n.a.createElement("div",{className:K.a.connecting},"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435",n.a.createElement("span",{className:K.a.connectingDot},"."),n.a.createElement("span",{className:K.a.connectingDot},"."),n.a.createElement("span",{className:K.a.connectingDot},".")))};var ae=function(){return n.a.createElement("div",{className:l.a.app},n.a.createElement(Q.a,{className:l.a.transparentSnackbar,maxSnack:1,anchorOrigin:{vertical:"top",horizontal:"center"},preventDuplicate:!0,autoHideDuration:3e3},n.a.createElement(te,null)))};var se=e=>{e&&e instanceof Function&&a.e(3).then(a.bind(null,54)).then(t=>{let{getCLS:a,getFID:s,getFCP:n,getLCP:i,getTTFB:r}=t;a(e),s(e),n(e),i(e),r(e)})};r.a.createRoot(document.getElementById("root")).render(n.a.createElement(ae,null)),se()},6:function(e,t,a){e.exports={inputContainer:"MessageInput_inputContainer__1Mj6U",AttachButton:"MessageInput_AttachButton__2Q40Z",attachedFiles:"MessageInput_attachedFiles__27RvM",attachedFileContainer:"MessageInput_attachedFileContainer__RbMfr",attachedFileCounterWeight:"MessageInput_attachedFileCounterWeight__3uSZy",attachedFile:"MessageInput_attachedFile__1OmXk",attachedFileCancel:"MessageInput_attachedFileCancel__31L5c",attachedFileCancelLine:"MessageInput_attachedFileCancelLine__1dBia",fileInput:"MessageInput_fileInput__3WHAv",TextArea:"MessageInput_TextArea__1Y39O",sendButtonContainer:"MessageInput_sendButtonContainer__21CGC"}},7:function(e,t,a){e.exports={userCard:"User_userCard__1QrEB",userInfoContainer:"User_userInfoContainer__3_pWZ",userIconContainer:"User_userIconContainer__1vxbk",userIcon:"User_userIcon__I8LB9",userInfo:"User_userInfo__3hRN_",userFullName:"User_userFullName__Nwv4f",additionInfo:"User_additionInfo__3iBKM",unreadCount:"User_unreadCount__1iS3E",count:"User_count__1c6nB"}}},[[29,1,2]]]);
//# sourceMappingURL=main.a28a0b00.chunk.js.map