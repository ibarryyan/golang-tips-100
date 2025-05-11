package code_33

import (
	"fmt"
	"github.com/go-playground/validator/v10"
	"testing"
)

type User struct {
	Age int `validate:"adult"`
}

func TestValidator(t *testing.T) {
	// 注册自定义校验规则
	validate := validator.New()
	_ = validate.RegisterValidation("adult", func(fl validator.FieldLevel) bool {
		return fl.Field().Int() >= 18
	})

	// 验证通过案例
	user := User{Age: 10}
	err := validate.Struct(user)
	if err != nil {
		fmt.Println(err)
	}
}
