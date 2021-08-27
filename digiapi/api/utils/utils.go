package utils

import "log"

func CaptureError(err error) {
	if err != nil {
		log.Fatalf("%s", err)
	}
}
