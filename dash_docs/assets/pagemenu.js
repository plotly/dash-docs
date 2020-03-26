if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.clientside = {
  pagemenu: function (children) {
    console.warn('updating pagemenu');
    return String(Date.now());
  }
}
