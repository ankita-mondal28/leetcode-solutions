/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Call the function immediately at time 0ms
    fn(...args);

    // Schedule repeated executions every t milliseconds
    const timerId = setInterval(() => {
        fn(...args);
    }, t);

    // Return a function that cancels the repeated execution
    return function cancelFn() {
        clearInterval(timerId);
    };
};

/**
 * Example Usage:
 * const result = [];
 * const fn = (x) => x * 2;
 * const args = [4], t = 35, cancelTimeMs = 190;
 *
 * const cancelFn = cancellable(fn, args, t);
 * setTimeout(cancelFn, cancelTimeMs);
 */