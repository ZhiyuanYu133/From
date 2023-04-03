/**
 * Select2 Japanese translation.
 */
(function ($) {
    "use strict";

    $.extend($.fn.select2.defaults, {
        formatNoMatches: function () { return "なし"; },
        formatInputTooShort: function (input, min) { var n = min - input.length; return "" + n + "れてください"; },
        formatInputTooLong: function (input, max) { var n = input.length - max; return "が" + n + "すぎます"; },
        formatSelectionTooBig: function (limit) { return "で" + limit + "までしかできません"; },
        formatLoadMore: function (pageNumber) { return "･･･"; },
        formatSearching: function () { return "･･･"; }
    });
})(jQuery);
