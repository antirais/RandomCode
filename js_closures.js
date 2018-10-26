/*
 * This is a JavaScript Clojure example.
 */

var tag = function(name, attrs){
    var attrs = attrs || {};
    
    var getAttrs = function(new_attrs){
        var _attrs = new_attrs || attrs;
        var attr_str = "";
        
       for(key in _attrs){
           attr_str += " "+key+"='"+_attrs[key].replace("'", "\\'")+"'";
       }
        
       return attr_str || "";
    }
        
    return function(data){
        var LT = "<",
            GT = ">",
            SL = "/";
        
        if('object' === typeof data){
            return tag(name, data);
        }
            
        return "<"+name+getAttrs(attrs)+">"+data+"</"+name+">";
    }
}

var wrap = function(data){
    for(arg in arguments){
        var func = arguments[arg];
        
        if('function' !== typeof func){
            continue;
        }
        
        data = func(data);
    };

    return data;
}

//Create tag with predefined attribute
var a = tag("a", {url: "test'er"});
//Creta plain tag
var u = tag("u");
var i = tag("i");
var div = tag("div");
var div_container = tag("div", {id: "container"});

//Print tag with predefined attribute
console.log(a("Clojure is nice"));
//Creat a new tag with new attributes
console.log(a({url:"http://example.com", class:"blinking"})("Clojures are epic!"));
console.log(a("Clojure is nice 2"));

//Wrap content in the following tags, override the attributes in the a ta
var wrapped_content = wrap("How cool can it get?", a({href:'http://google.com'}), u, i, div({style:"background-color:red;"}), div_container);
console.log(wrapped_content);

var body = document.getElementsByTagName("html")[0];
body.innerHTML = wrapped_content;

