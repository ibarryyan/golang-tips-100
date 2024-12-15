package code_25

import (
	"github.com/gin-gonic/gin"
	"log"
	"time"
)

// 自定义日志中间件
func LoggerMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()
		// 处理请求
		c.Next()
		// 请求结束后记录日志
		duration := time.Since(start)
		log.Printf("Request %s %s took %v", c.Request.Method, c.Request.URL.Path, duration)
	}
}

func main() {
	r := gin.New()
	// 使用自定义中间件
	r.Use(LoggerMiddleware())

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.Run(":8080")
}
