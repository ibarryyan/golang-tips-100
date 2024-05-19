package main

import (
	"fmt"
	"github.com/go-co-op/gocron/v2"
	"time"
)

func Run() {
	s, err := gocron.NewScheduler()
	if err != nil {
		fmt.Printf("gocron.NewScheduler err : %v", err)
		return
	}

	_, err = s.NewJob(gocron.CronJob("* * * * * *", true), gocron.NewTask(
		func() {
			fmt.Printf("CronJob , time : %v \n", time.Now().Format("2006-01-02 15:04:05"))
		},
	))
	if err != nil {
		fmt.Printf("NewJob err : %v", err)
		return
	}

	_, err = s.NewJob(gocron.DurationJob(3*time.Second), gocron.NewTask(
		func() {
			fmt.Printf("DurationJob , time : %v \n", time.Now().Format("2006-01-02 15:04:05"))
		},
	))
	if err != nil {
		fmt.Printf("NewJob err : %v", err)
		return
	}

	s.Start()
	select {}
}
