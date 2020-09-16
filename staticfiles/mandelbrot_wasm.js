let wasm;

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
    * @returns {number}
    */
    height() {
        var ret = wasm.application_height(this.ptr);
        return ret >>> 0;
    }
    /**
    * @returns {number}
    */
    width() {
        var ret = wasm.application_width(this.ptr);
        return ret >>> 0;
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
    */
    reset() {
        wasm.application_reset(this.ptr);
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
    /**
    * @returns {number}
    */
    image_buffer() {
        var ret = wasm.application_image_buffer(this.ptr);
        return ret;
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

    static __wrap(ptr) {
        const obj = Object.create(Point.prototype);
        obj.ptr = ptr;

        return obj;
    }

    free() {
        const ptr = this.ptr;
        this.ptr = 0;

        wasm.__wbg_point_free(ptr);
    }
    /**
    * @param {number} x
    * @param {number} y
    * @returns {Point}
    */
    static new(x, y) {
        var ret = wasm.point_new(x, y);
        return Point.__wrap(ret);
    }
}

async function load(module, imports) {
    if (typeof Response === 'function' && module instanceof Response) {

        if (typeof WebAssembly.instantiateStreaming === 'function') {
            try {
                return await WebAssembly.instantiateStreaming(module, imports);

            } catch (e) {
                if (module.headers.get('Content-Type') != 'application/wasm') {
                    console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n", e);

                } else {
                    throw e;
                }
            }
        }

        const bytes = await module.arrayBuffer();
        return await WebAssembly.instantiate(bytes, imports);

    } else {

        const instance = await WebAssembly.instantiate(module, imports);

        if (instance instanceof WebAssembly.Instance) {
            return { instance, module };

        } else {
            return instance;
        }
    }
}

async function init(input) {
    if (typeof input === 'undefined') {
        input = import.meta.url.replace(/\.js$/, '_bg.wasm');
    }
    const imports = {};
    imports.wbg = {};
    imports.wbg.__wbindgen_throw = function(arg0, arg1) {
        throw new Error(getStringFromWasm0(arg0, arg1));
    };

    if (typeof input === 'string' || (typeof Request === 'function' && input instanceof Request) || (typeof URL === 'function' && input instanceof URL)) {
        input = fetch(input);
    }

    const { instance, module } = await load(await input, imports);

    wasm = instance.exports;
    init.__wbindgen_wasm_module = module;

    return wasm;
}

export default init;

