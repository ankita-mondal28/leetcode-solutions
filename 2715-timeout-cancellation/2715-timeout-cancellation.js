/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Schedule fn to run after t milliseconds
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);

    // Return a function that cancels the scheduled execution
    return function cancelFn() {
        clearTimeout(timerId);
    };
};

/**
 * Example Usage:
 * const result = [];
 * const fn = (x) => x * 5;
 * const args = [2], t = 20, cancelTimeMs = 50;
 * 
 * const cancelFn = cancellable(fn, args, t);
 * setTimeout(cancelFn, cancelTimeMs);
 */