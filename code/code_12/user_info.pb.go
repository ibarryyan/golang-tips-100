// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.31.0
// 	protoc        v3.21.5
// source: user_info.proto

package code_12

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type UserInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// Types that are assignable to Address:
	//
	//	*UserInfo_SchoolAddr
	//	*UserInfo_HomeAddr
	Address isUserInfo_Address `protobuf_oneof:"address"`
}

func (x *UserInfo) Reset() {
	*x = UserInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_user_info_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UserInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UserInfo) ProtoMessage() {}

func (x *UserInfo) ProtoReflect() protoreflect.Message {
	mi := &file_user_info_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UserInfo.ProtoReflect.Descriptor instead.
func (*UserInfo) Descriptor() ([]byte, []int) {
	return file_user_info_proto_rawDescGZIP(), []int{0}
}

func (x *UserInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (m *UserInfo) GetAddress() isUserInfo_Address {
	if m != nil {
		return m.Address
	}
	return nil
}

func (x *UserInfo) GetSchoolAddr() string {
	if x, ok := x.GetAddress().(*UserInfo_SchoolAddr); ok {
		return x.SchoolAddr
	}
	return ""
}

func (x *UserInfo) GetHomeAddr() string {
	if x, ok := x.GetAddress().(*UserInfo_HomeAddr); ok {
		return x.HomeAddr
	}
	return ""
}

type isUserInfo_Address interface {
	isUserInfo_Address()
}

type UserInfo_SchoolAddr struct {
	SchoolAddr string `protobuf:"bytes,2,opt,name=school_addr,json=schoolAddr,proto3,oneof"`
}

type UserInfo_HomeAddr struct {
	HomeAddr string `protobuf:"bytes,3,opt,name=home_addr,json=homeAddr,proto3,oneof"`
}

func (*UserInfo_SchoolAddr) isUserInfo_Address() {}

func (*UserInfo_HomeAddr) isUserInfo_Address() {}

var File_user_info_proto protoreflect.FileDescriptor

var file_user_info_proto_rawDesc = []byte{
	0x0a, 0x0f, 0x75, 0x73, 0x65, 0x72, 0x5f, 0x69, 0x6e, 0x66, 0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x03, 0x63, 0x6d, 0x64, 0x22, 0x6b, 0x0a, 0x08, 0x55, 0x73, 0x65, 0x72, 0x49, 0x6e,
	0x66, 0x6f, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x21, 0x0a, 0x0b, 0x73, 0x63, 0x68, 0x6f, 0x6f, 0x6c,
	0x5f, 0x61, 0x64, 0x64, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0a, 0x73,
	0x63, 0x68, 0x6f, 0x6f, 0x6c, 0x41, 0x64, 0x64, 0x72, 0x12, 0x1d, 0x0a, 0x09, 0x68, 0x6f, 0x6d,
	0x65, 0x5f, 0x61, 0x64, 0x64, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x08,
	0x68, 0x6f, 0x6d, 0x65, 0x41, 0x64, 0x64, 0x72, 0x42, 0x09, 0x0a, 0x07, 0x61, 0x64, 0x64, 0x72,
	0x65, 0x73, 0x73, 0x42, 0x0a, 0x5a, 0x08, 0x2f, 0x63, 0x6f, 0x64, 0x65, 0x5f, 0x31, 0x32, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_user_info_proto_rawDescOnce sync.Once
	file_user_info_proto_rawDescData = file_user_info_proto_rawDesc
)

func file_user_info_proto_rawDescGZIP() []byte {
	file_user_info_proto_rawDescOnce.Do(func() {
		file_user_info_proto_rawDescData = protoimpl.X.CompressGZIP(file_user_info_proto_rawDescData)
	})
	return file_user_info_proto_rawDescData
}

var file_user_info_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_user_info_proto_goTypes = []interface{}{
	(*UserInfo)(nil), // 0: cmd.UserInfo
}
var file_user_info_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_user_info_proto_init() }
func file_user_info_proto_init() {
	if File_user_info_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_user_info_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UserInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_user_info_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*UserInfo_SchoolAddr)(nil),
		(*UserInfo_HomeAddr)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_user_info_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_user_info_proto_goTypes,
		DependencyIndexes: file_user_info_proto_depIdxs,
		MessageInfos:      file_user_info_proto_msgTypes,
	}.Build()
	File_user_info_proto = out.File
	file_user_info_proto_rawDesc = nil
	file_user_info_proto_goTypes = nil
	file_user_info_proto_depIdxs = nil
}
