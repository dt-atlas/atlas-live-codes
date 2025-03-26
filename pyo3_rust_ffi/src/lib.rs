use pyo3::prelude::*;

#[pyfunction]
fn average(values: Vec<f64>) -> PyResult<f64> {
    let count: f64 = values.len() as f64;
    let sum: f64 = values.iter().sum();
    Ok(sum / count)
}

// the trait bound `&Vec<f64>: PyFunctionArgument<'_, '_>` is not satisfied
// the following other types implement trait `PyFunctionArgument<'a, 'py>`:
//   &'a pyo3::Bound<'py, T>
//   Option<&'a pyo3::Bound<'py, T>>

/// A Python module implemented in Rust.
#[pymodule]
fn pyo3_rust_ffi(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(average, m)?)?;
    Ok(())
}
