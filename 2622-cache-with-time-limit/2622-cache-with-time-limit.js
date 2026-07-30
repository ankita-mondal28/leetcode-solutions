var TimeLimitedCache = function() {
    this.cache = new Map(); // Stores key -> { value, timerId }
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = this.cache.has(key);

    // If key already exists, clear its previous expiration timer
    if (exists) {
        clearTimeout(this.cache.get(key).timerId);
    }

    // Set a new expiration timer to delete the key when time is up
    const timerId = setTimeout(() => {
        this.cache.delete(key);
    }, duration);

    // Store the value and the timer reference
    this.cache.set(key, { value, timerId });

    return exists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache.has(key)) {
        return this.cache.get(key).value;
    }
    return -1;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * Example Usage:
 * const cache = new TimeLimitedCache();
 * cache.set(1, 42, 1000); // returns false
 * cache.get(1);           // returns 42
 * cache.count();         // returns 1
 */