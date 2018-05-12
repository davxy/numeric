function test = allclose(a,b,tol)
  % Check that all matrix elements are close enough
  res = isclose(a,b,tol);
  test = all(res(:) == 1);
  return
end
