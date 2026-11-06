var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
var __commonJS = (cb, mod) => function __require() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __publicField = (obj, key, value) => __defNormalProp(obj, typeof key !== "symbol" ? key + "" : key, value);

// node_modules/mark.js/dist/mark.js
var require_mark = __commonJS({
  "node_modules/mark.js/dist/mark.js"(exports, module) {
    (function(global, factory) {
      typeof exports === "object" && typeof module !== "undefined" ? module.exports = factory() : typeof define === "function" && define.amd ? define(factory) : global.Mark = factory();
    })(exports, (function() {
      "use strict";
      var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function(obj) {
        return typeof obj;
      } : function(obj) {
        return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj;
      };
      var classCallCheck = function(instance, Constructor) {
        if (!(instance instanceof Constructor)) {
          throw new TypeError("Cannot call a class as a function");
        }
      };
      var createClass = /* @__PURE__ */ (function() {
        function defineProperties(target, props) {
          for (var i = 0; i < props.length; i++) {
            var descriptor = props[i];
            descriptor.enumerable = descriptor.enumerable || false;
            descriptor.configurable = true;
            if ("value" in descriptor) descriptor.writable = true;
            Object.defineProperty(target, descriptor.key, descriptor);
          }
        }
        return function(Constructor, protoProps, staticProps) {
          if (protoProps) defineProperties(Constructor.prototype, protoProps);
          if (staticProps) defineProperties(Constructor, staticProps);
          return Constructor;
        };
      })();
      var _extends = Object.assign || function(target) {
        for (var i = 1; i < arguments.length; i++) {
          var source = arguments[i];
          for (var key in source) {
            if (Object.prototype.hasOwnProperty.call(source, key)) {
              target[key] = source[key];
            }
          }
        }
        return target;
      };
      var DOMIterator = (function() {
        function DOMIterator2(ctx) {
          var iframes = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : true;
          var exclude = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : [];
          var iframesTimeout = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : 5e3;
          classCallCheck(this, DOMIterator2);
          this.ctx = ctx;
          this.iframes = iframes;
          this.exclude = exclude;
          this.iframesTimeout = iframesTimeout;
        }
        createClass(DOMIterator2, [{
          key: "getContexts",
          value: function getContexts() {
            var ctx = void 0, filteredCtx = [];
            if (typeof this.ctx === "undefined" || !this.ctx) {
              ctx = [];
            } else if (NodeList.prototype.isPrototypeOf(this.ctx)) {
              ctx = Array.prototype.slice.call(this.ctx);
            } else if (Array.isArray(this.ctx)) {
              ctx = this.ctx;
            } else if (typeof this.ctx === "string") {
              ctx = Array.prototype.slice.call(document.querySelectorAll(this.ctx));
            } else {
              ctx = [this.ctx];
            }
            ctx.forEach(function(ctx2) {
              var isDescendant = filteredCtx.filter(function(contexts) {
                return contexts.contains(ctx2);
              }).length > 0;
              if (filteredCtx.indexOf(ctx2) === -1 && !isDescendant) {
                filteredCtx.push(ctx2);
              }
            });
            return filteredCtx;
          }
        }, {
          key: "getIframeContents",
          value: function getIframeContents(ifr, successFn) {
            var errorFn = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : function() {
            };
            var doc = void 0;
            try {
              var ifrWin = ifr.contentWindow;
              doc = ifrWin.document;
              if (!ifrWin || !doc) {
                throw new Error("iframe inaccessible");
              }
            } catch (e) {
              errorFn();
            }
            if (doc) {
              successFn(doc);
            }
          }
        }, {
          key: "isIframeBlank",
          value: function isIframeBlank(ifr) {
            var bl = "about:blank", src = ifr.getAttribute("src").trim(), href = ifr.contentWindow.location.href;
            return href === bl && src !== bl && src;
          }
        }, {
          key: "observeIframeLoad",
          value: function observeIframeLoad(ifr, successFn, errorFn) {
            var _this = this;
            var called = false, tout = null;
            var listener = function listener2() {
              if (called) {
                return;
              }
              called = true;
              clearTimeout(tout);
              try {
                if (!_this.isIframeBlank(ifr)) {
                  ifr.removeEventListener("load", listener2);
                  _this.getIframeContents(ifr, successFn, errorFn);
                }
              } catch (e) {
                errorFn();
              }
            };
            ifr.addEventListener("load", listener);
            tout = setTimeout(listener, this.iframesTimeout);
          }
        }, {
          key: "onIframeReady",
          value: function onIframeReady(ifr, successFn, errorFn) {
            try {
              if (ifr.contentWindow.document.readyState === "complete") {
                if (this.isIframeBlank(ifr)) {
                  this.observeIframeLoad(ifr, successFn, errorFn);
                } else {
                  this.getIframeContents(ifr, successFn, errorFn);
                }
              } else {
                this.observeIframeLoad(ifr, successFn, errorFn);
              }
            } catch (e) {
              errorFn();
            }
          }
        }, {
          key: "waitForIframes",
          value: function waitForIframes(ctx, done) {
            var _this2 = this;
            var eachCalled = 0;
            this.forEachIframe(ctx, function() {
              return true;
            }, function(ifr) {
              eachCalled++;
              _this2.waitForIframes(ifr.querySelector("html"), function() {
                if (!--eachCalled) {
                  done();
                }
              });
            }, function(handled) {
              if (!handled) {
                done();
              }
            });
          }
        }, {
          key: "forEachIframe",
          value: function forEachIframe(ctx, filter, each) 