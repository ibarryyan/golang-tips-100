package code_12

import (
	"encoding/json"
	"fmt"
	"testing"
)

func TestJSONMarshal(t *testing.T) {

	u := UserInfo{
		Name:    "zs",
		Address: &UserInfo_HomeAddr{HomeAddr: "Beijing"},
	}

	marshal, _ := json.Marshal(u)

	fmt.Println(string(marshal))

	var u2 UserInfo

	_ = json.Unmarshal(marshal, &u2)

	fmt.Println(u2)
}

func TestProtoMarshal(t *testing.T) {
	u := UserInfo{
		Name:    "zs",
		Address: &UserInfo_HomeAddr{HomeAddr: "Beijing"},
	}

	marshal, _ := proto.Marshal(u)

	fmt.Println(string(marshal))

	var u2 UserInfo

	_ = proto.Unmarshal(marshal, u2)

	fmt.Println(u2)
}
