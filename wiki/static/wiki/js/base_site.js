<!-- This is for Article View -->
function parse_and_set_linenos() {
  linenos = $(".linenos").find("pre");
  if (!linenos.length) return;
  lines = linenos.html().split("\n").length;
  i = 0;
  maxdigits = String(lines).length;
  linenos.empty();
  while (lines-- && ++i) {
    spaces = maxdigits - String(i).length + 1;
    a = (function(i){
      return $("<a id='L" + i + "' href='#L" + i + "'>" + Array(spaces).join(' ') + i + "</a><br/>");
    })(i);
    a.css("text-align", "right");
    linenos.append(a);
  }
}
function footer_set_at_bottom() {
  var calc = $(document).height() - $('.wiki-navbar').outerHeight() - $('#article-breadcrumbs').outerHeight() - $('#article-container').outerHeight() - $('footer').outerHeight();
  if ($(document).height() == $(window).height())
    if (calc > 0)
      $('footer').css('margin-top', calc);
  return true;
}
$(function(){
  parse_and_set_linenos();
  /*footer_set_at_bottom();*/
});




<!-- This is for Create and Edit View -->

//<![CDATA[ 
/* tabs in editor and article markup bar hide/show */
function applytabchars() {
  var language = $("#id_language").val();
  var tab_chars = $("#tab-chars").val()
  $(".wiki-control textarea").css("tab-size", tab_chars);
}
function show_hide_markup_options() {
  var el = this;
  if (el == window)
    el = $("#id_language");
  val = $(el).val();
  if (val == null || typeof val == "undefined") {
    /*try from url*/
    var ma = window.location.pathname.match('^/wiki/([^/]+)/.+');
    val = ma && ma.constructor==Array && ma.length>1 ? ma[1] : null;
  }
  if (val == "_") {
    $(".markItUpHeader").show();
    window.markItUpHeaderShow = window.setTimeout(
      function(){$(".markItUpHeader").show();},
      1000);
  }
  else {
    window.clearTimeout(window.markItUpHeaderShow);
    $(".markItUpHeader").hide();
  }
}
(function($) {
  $(document).ready(function (){
    /*$("#id_title").keyup(function () {
      var e = $("#id_slug")[0];
      if(!e._changed) {
        slug = URLify(this.value, 50);
        e.value = slug;
      }
      });*/
  $("#id_language").on('change', show_hide_markup_options);
  $("#id_language").on('change', applytabchars);
  show_hide_markup_options();
  /* TAB is \t inside text area */
  /* code shamelessly copied from http://stackoverflow.com/questions/6637341 */
  $(document).delegate('.wiki-control textarea', 'keydown', function(e) {
    var keyCode = e.keyCode || e.which;

    if (keyCode == 9) {
      e.preventDefault();
      var start = $(this).get(0).selectionStart;
      var end = $(this).get(0).selectionEnd;

      // set textarea value to: text before caret + tab + text after caret
      $(this).val($(this).val().substring(0, start)
                  + "\t"
                  + $(this).val().substring(end));

      // put caret at right position again
      $(this).get(0).selectionStart =
      $(this).get(0).selectionEnd = start + 1;
    }
  });
  var tab_html = '\
  <div id="tab-div" style="display: inline-flex; float: right;">\
  Tabs are\
  <input id="tab-chars" type="number" style="width: 2em; margin-left: 1em; margin-right: 1em;"\
  maxlength="1" value="8" disabled="disabled">\
  characters wide\
  </div>';
  $("#div_id_content .wiki-label").append($(tab_html));
  $("#tab-chars").on('change', applytabchars);
  applytabchars();
});
})(jQuery);
//]]>




<!-- This is for the homepage -->

function reddit_hn_top_init (){
  window.wikicoding = window.wikicoding || {};
  if (!window.wikicoding.reddit_hn_top_flag)
    return
  /* reddit */
  var d;
  window.wikicoding.reddit_ajax = $.ajax('http://www.reddit.com/r/programming/top.json?limit=10')
    .done(function(x){
      d=x.data.children;
      var divlist = [];
      $.each(d, function(i, v) {
        v = v.data;
        var div = $("<div class='rh'/>");
        var a = $("<a target='_blank' href='"+v.url+"'>"+v.title+"</a>");
        var c = $("<a target='_blank' style='font-style:italic;font-size:0.8em' href='http://reddit.com"+v.permalink+"'>"+v.num_comments+" comments</a>");
        div.append(a)
           .append($("<br/>"))
           .append($(document.createTextNode('(')))
           .append(c)
           .append($(document.createTextNode(')')));
        divlist.push(div);
      });
      $(".reddit-top").append(divlist);
    });

  /* hacker news */
  /* copied from SO and modified. no time for js */
  window.wikicoding.hn_ajax = $.getJSON('//hacker-news.firebaseio.com/v0/topstories.json?callback=?', function(json) {
      var $div = $('<div/>').appendTo($(".hn-top"));
      for (var i = 0; i < Math.min(json.length, 10); i++) {
          (function(i) {
              var $a = $("<a target='_blank' />");
              var $c = $("<a target='_blank' style='font-style:italic;font-size:0.8em' href='https://news.ycombinator.com/item?id="+json[i]+"'/>");
              $.getJSON('https://hacker-news.firebaseio.com/v0/item/' + json[i] + '.json', function(j) {
                  if (j.url)
                    $a.attr('href', j.url).text(j.title);
                  else
                    $a.attr('href', "https://news.ycombinator.com/item?id=" + j.id).text(j.title);
                  $c.text(j.descendants + " comments");
              });
              $('<div  class="rh"/>').append($a)
                         .append($("<br/>"))
                         .append($(document.createTextNode('(')))
                         .append($c)
                         .append($(document.createTextNode(')')))
                         .appendTo($div);
          })(i);
      }
  });
}
$(reddit_hn_top_init);
