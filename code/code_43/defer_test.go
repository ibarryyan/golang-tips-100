package code_43

func test1() int {
	var i int = 1
	defer func() {
		i++
	}()
	return i
}

func test2() (i int) {
	i = 1
	defer func() {
		i++
	}()
	return i
}
