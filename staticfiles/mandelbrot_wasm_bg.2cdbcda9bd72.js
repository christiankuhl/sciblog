import * as wasm from './mandelbrot_wasm_bg.wasm';

let cachedTextDecoder = new TextDecoder('utf-8', { ignoreBOM: true, fatal: true });

cachedTextDecoder.decode();

let cachegetUint8Memory0 = null;
function getUint8Memory0() {
    if (cachegetUint8Memory0 === null || cachegetUint8Memory0.buffer !== wasm.memory.buffer) {
        cachegetUint8Memory0 = new Uint8Array(wasm.memory.buffer);
    }
    return cachegetUint8Memory0;
}

function getStringFromWasm0(ptr, len) {
    return cachedTextDecoder.decode(getUint8Memory0().subarray(ptr, ptr + len));
}

function _assertClass(instance, klass) {
    if (!(instance instanceof klass)) {
        throw new Error(`expected instance of ${klass.name}`);
    }
    return instance.ptr;
}
/**
*/
export const Key = Object.freeze({ Up:0,"0":"Up",Down:1,"1":"Down",Left:2,"2":"Left",Right:3,"3":"Right", });
/**
*/
export class Application {

    static __wrap(ptr) {
        const obj = Object.create(Application.prototype);
        obj.ptr = ptr;

        return obj;
    }

    free() {
        const ptr = this.ptr;
        this.ptr = 0;

        wasm.__wbg_application_free(ptr);
    }
    /**
    * @returns {Application}
    */
    static new() {
        var ret = wasm.application_new();
        return Application.__wrap(ret);
    }
    /**
    */
    update() {
        wasm.application_update(this.ptr);
    }
    /**
    * @param {Point} point
    * @param {boolean} out
    */
    zoom(point, out) {
        _assertClass(point, Point);
        var ptr0 = point.ptr;
        point.ptr = 0;
        wasm.application_zoom(this.ptr, ptr0, out);
    }
    /**
    * @param {number} direction
    */
    shift(direction) {
        wasm.application_shift(this.ptr, direction);
    }
}
/**
*/
export class ApplicationSettings {

    free() {
        const ptr = this.ptr;
        this.ptr = 0;

        wasm.__wbg_applicationsettings_free(ptr);
    }
}
/**
*/
export class Point {

    free() {
        const ptr = this.ptr;
        this.ptr = 0;

        wasm.__wbg_point_free(ptr);
    }
}

export const __wbindgen_throw = function(arg0, arg1) {
    throw new Error(getStringFromWasm0(arg0, arg1));
};

