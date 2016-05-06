var $beResizePics = {
                      "Obj": ['body','.act-title','.bubble-block .title'],
                      "Style": {
                        'body': ['font-size'],
                        '.act-title': ['width'],
                        '.bubble-block .title': ['width']
                      },
                      "Options": {
                        'body': ['none'],
                        '.act-title': ['init-use'],
                        '.bubble-block .title': ['init-use']
                      }
                    };
var $beResizePicsMin = {
                      "Obj": ['body','.act-title'],
                      "Style": {
                        'body': ['font-size'],
                        '.act-title': ['width']
                      },
                      "Options": {
                        'body': ['none'],
                        '.act-title': ['no-resize']
                      }
                    };
$(document).ready(function(){
  setOriginalData();
  resizes();
  $(window).resize(function(){
    resizes();
  });
});

function setOriginalData() {
  $($beResizePics["Obj"]).each(function(k,v){
    $($beResizePics["Style"][v]).each(function(k1,v1){
      $(v).data(v1,$(v).css(v1)); // get original Style insert to data
    });
  });
}

function resizes() {
  if (1000 > $(window).width()) {
    if (640 >= $(window).width()) {
      var $percentage = ($(window).width()/640)*100 + '%';
      var $resizes = $beResizePicsMin;
    } else {
      var $percentage = ($(window).width()/1000)*100 + '%';
      var $resizes = $beResizePics;
    }
    $($resizes["Obj"]).each(function(k,v){
      $($resizes["Style"][v]).each(function(k1,v1){
        $(v).css(
          v1, function(index){
            switch ($resizes["Options"][v][k1]) {
              case 'init-use':
                return parseInt($(v).data(v1)) * parseInt($percentage) / 100 + 'px';
                break;
              case 'no-resize':
                return '';
                break;
              default:
                return $percentage;
            }
          }
        );
      });
    });
  } else {
    $($beResizePics["Obj"]).each(function(k,v){
      $($beResizePics["Style"][v]).each(function(k1,v1){
        $(v).css(
          v1, function(index){
            return '';
          }
        );
      });
    });
  }
}

(function($){ 
  $(document).ready(function(){ // IE8 升級提醒，請勿刪除
    if (typeof navigator.geolocation === 'undefined') {
      var $html = '<div id="browser-upgrade-reminds">' +
                  '  <div class="close" style="position: absolute; top: -13px; right: -13px; background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpEMTA0MzU1MEMwRjYxMUU1ODBGRkVFODkzMTA4Q0U3NiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpEMTA0MzU1MUMwRjYxMUU1ODBGRkVFODkzMTA4Q0U3NiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkQxMDQzNTRFQzBGNjExRTU4MEZGRUU4OTMxMDhDRTc2IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkQxMDQzNTRGQzBGNjExRTU4MEZGRUU4OTMxMDhDRTc2Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+tIesgQAABUNJREFUeNq0WH1MW1UUP33f7SstdLC2CHQ0AxXZ1FinEx2NTfzYtMlITHT+RUIi0WQJiSaOZNFkxrH4wZxOlziyaYxxyIgB0UxHJGwNyVI0Cgtu3fqRFmjBUQaylva19d7H2lH6Cl3BX/LS1757zu/3zj3n3nsq6+zsBJKkQCaTQTweB4AEYJAkKX4m0NdQKAQMRVXxY9fqFJcdJs7hroVYrJL1TWplIIPFcn0ASMI1W64f9WqL7FMGvY1mOUdpqR7C4UUoLCxEfuKiL4oiERcBgiCIXBQmJwgCXUkBSxCEGDAMDVNjV8yl5y426MecViIUNkAGEsB6xivQTYXW6a3XoptFmvRM11b3TD73VHeQgAGe528TA9IdQ0JiwLIMRKMCyLq6zopOsDr8IyaOx2Mgi0SNm34aaFL9cqGRWIzoIA8INOV3mx44df2JB08W6XROjUaT9hxHmUqGHKuLRCIoEiRwt8KW4o87WjiXdw+sA1RU0G0d+vNAiXtiu6d5X7ugEvopiko9x9EgaJrG9OitcRTQnLi9Vt07R9vWS74c6snpPTVHT7epp4PWZG4lQeCQB4MzcPXqFYhMTllKPzl9kJqZNcEGgwreNJV89OVBmJm1pAmYnBgHr9cLKrnCWNze0ULNzm04+R0Rcyb9p1+3yISYMSVApVYDy7DAnelt0s7MZYSdVBWA+oVngCkrzZkIj8U22HYl8NRqevubUgJwnd7DcGaTO9CYQV6khuoLPbDlm+Nw3+/noeilF9ckx2PwWGyDbbGPjJz49WIjioZZFDAx7oPN520NUqWm3LUTGEPZUpWgNaH8xAerisDP8Bg8VowEssU+VgJzaX4eaBDvlSRVpR2+bJVyGB4Zg0QkmvouQxmcTUSKfFmWY1vsQwrKwUtWCIWriMJRRx0pxAxSgxadHvDub4UEqtfVREiSIxtsi31IgYgKBm54pI5Su8dXzfrgdz+In+XH21IESRFJSJK/8XbKNhtUTq+JekitqV0AD6xHRD7kYo74/LUUClFlLqWVTUTatnQX5Bj01I1KIjY3r821vrFjTLA8J/IlF/MgFNYSd72cSZDn9CybCLRaBXIdLJXtuZRoNsTlXIBgjQZXvuQ47GuV6GqIbt7kIriae0fzJfc2vyVe+YqIlOlGCb5uhz1f8uD3veKVr4hoTbWdUO+22AiOk1wI2KpKVHZHspKnqiObCGSLfUghwdCem9uqbQTBKxxFrzb0SA1C05PaWLKRryoC2WIfUph78tGeOMs4xDLUvvl6NxLiXzno38EhiPgmUhtLNvIMEbc3MGyLfWRkP8v4Z56v78ZHcxk+B2L432t/P/Dh5wekDiSqZ82wMDScEpPLgYTf+QjMnRsAtNBlPL+x23x4ymppFaOUFBAPh40O895j4b+vbdhhVHKH1ZX0OVub9ydo2okjkFoJUSI6t3x7op0q1tj/L3JBqbC7X3u5XSAIJ24BcCOUthSjRanf2NVxiNZrN1xERK20O5tfORTSqPuj0ajYDioUijtTkKY0MG1x7WtuuTX814ZMx3yZrs/RuBc1JgViYyKXc0gALbaDkgKSORE48lnTP1981Yju82rNYhTp9z62/ZTv6cdPyuSck+M4RC4H3AzhZhg3KVkFLIuG2X/4WMNsd58VZbQhp3AzlMe3taLner2pO1aoGlAgUoWCBw69OY4ATTNiQ5xWBWsB1XbV/G+2uvn+QdPCpT/E9jw0MiaeJeTb7kftOenidzw8WmDZZX/3x7M2lucdcrkCeF4BSqUSWPT2LMuKb7/0d8CS3/8EGAC5W4nhnWLyhAAAAABJRU5ErkJggg==) no-repeat 0 0; width: 34px; height: 34px; cursor: pointer;"></div>' +
                  '  <div style="width: 530px; background-color: #fff; border: 1px solid #dddddd; padding: 20px 25px; -moz-border-radius: 5px; -webkit-border-radius: 5px; border-radius: 5px;">' +
                  '    <h2 style="border-bottom: 2px solid #e8362c; padding-bottom: 5px; padding-left: 5px; font-family: \'微軟正黑體\', \'新細明體\', Arial, Helvetica, sans-serif; font-size: 20px; font-weight: 700; line-height: 1.5em;">建議您升級瀏覽器版本或調整檢視設定</h2>' +
                  '    <div style="background: url(data:image/png;base64,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) no-repeat 22px 26px; padding-left: 146px; padding-right: 48px; height: 150px; font-size: 16px; line-height: 24px;">' +
                  '      <p style="padding-top: 30px; text-align: justify;">永豐銀行網路服務安全再升級，讓交易更放心，建議您更新瀏覽器版本為 IE9.0 (含)以上版本或使用 Chrome、Firefox、Safari 等最新版本瀏覽器，謝謝!</p>' +
                  '    </div>' +
                  '    <div style="clear: both; margin: 0 auto; text-align: center;">' +
                  '      <a target="_blank" href="https://mma.sinopac.com/Bank/BankFrame.aspx?url=browser/upgrade.html" style="display: inline-block; background: #f31e36; color: #fff; font-weight: bold; font-size: 18px; line-height: 24px; border: 0; filter: progid:DXImageTransform.Microsoft.gradient(gradientType=0, startColorstr=\'#FFC43343\', endColorstr=\'#FF8B0212\'); background-image: url(\'data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgi…pZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9InVybCgjZ3JhZCkiIC8+PC9zdmc+IA==\'); background-size: 100%; background-image: -webkit-gradient(linear, 50% 0%, 50% 100%, color-stop(0%, #c43343), color-stop(100%, #8b0212)); background-image: -moz-linear-gradient(top, #c43343 0%, #8b0212 100%); background-image: -webkit-linear-gradient(top, #c43343 0%, #8b0212 100%); background-image: linear-gradient(to bottom, #c43343 0%, #8b0212 100%); width: 200px; margin: 10px 0; zoom: 1; padding: 8px 30px; border-radius: 5px; box-shadow: 0px 1px 1px rgba(180, 178, 178, 0.5), inset 0px 0px 0px rgba(255, 255, 255, 0.7); background: -moz-linear-gradient(top, #ffffff 0%, #ffffff 25%, #efefef);">立即升級</a>' +
                  '    </div>' +
                  '  </div>' +
                  '</div>';
      $('body').append($html);
      $('#browser-upgrade-reminds').lightbox_me();
    }
  });
})(jQuery);

/**
 * jQuery.support.cssProperty
 * To verify that a CSS property is supported (or any of its browser-specific implementations)
 *
 * @param string p - css property name
 * [@param] bool rp - optional, if set to true, the css property name will be returned, instead of a boolean support indicator
 *
 * @Author: Axel Jack Fuchs (Cologne, Germany)
 * @Date: 08-29-2010 18:43
 *
 * Example: $.support.cssProperty('boxShadow');
 * Returns: true
 *
 * Example: $.support.cssProperty('boxShadow', true);
 * Returns: 'MozBoxShadow' (On Firefox4 beta4)
 * Returns: 'WebkitBoxShadow' (On Safari 5)
 */
$.support.cssProperty = (function() {
  function cssProperty(p, rp) {
    var b = document.body || document.documentElement,
        s = b.style;

    // No css support detected
    if(typeof s == 'undefined') { return false; }

    // Tests for standard prop
    if(typeof s[p] == 'string') { return rp ? p : true; }

    // Tests for vendor specific prop
    var v = ['Moz', 'Webkit', 'Khtml', 'O', 'ms', 'Icab'],
        p = p.charAt(0).toUpperCase() + p.substr(1);
    
    for(var i=0; i<v.length; i++) {
        if(typeof s[v[i] + p] == 'string') { return rp ? (v[i] + p) : true; }
    }

    return false;
  }

  return cssProperty;
})();