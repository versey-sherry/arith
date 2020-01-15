load harness

@test "subtration-1" {
  check '3-2' '-1'
}

@test "subtration-2" {
  check '90-3' '87'
}

@test "subtration-3" {
  check '1 - 0' '1'
}

@test "subtration-4" {
  check '-1 - 3' '-4'
}

@test "subtration-multiple-1" {
  check '45-3 -4 -7' '31'
}

@test "subtration-multiple-2" {
  check '10 -3 -1 ' '6'
}

@test "asubtration-multiple-3" {
  check '-1 - -2 - 3' '-6'
}
