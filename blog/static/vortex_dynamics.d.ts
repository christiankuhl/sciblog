/* tslint:disable */
/* eslint-disable */
/**
*/
export class NVortexProblem {
  free(): void;
/**
* @param {Float64Array} gamma
* @param {Float64Array} z
* @returns {NVortexProblem}
*/
  static new(gamma: Float64Array, z: Float64Array): NVortexProblem;
/**
* @param {number} t_max
* @returns {Float64Array}
*/
  mesh(t_max: number): Float64Array;
}

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
  readonly memory: WebAssembly.Memory;
  readonly __wbg_nvortexproblem_free: (a: number) => void;
  readonly nvortexproblem_new: (a: number, b: number, c: number, d: number) => number;
  readonly nvortexproblem_mesh: (a: number, b: number, c: number) => void;
  readonly __wbindgen_malloc: (a: number) => number;
  readonly __wbindgen_free: (a: number, b: number) => void;
}

/**
* If `module_or_path` is {RequestInfo} or {URL}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {InitInput | Promise<InitInput>} module_or_path
*
* @returns {Promise<InitOutput>}
*/
export default function init (module_or_path?: InitInput | Promise<InitInput>): Promise<InitOutput>;
        