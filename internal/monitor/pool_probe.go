package monitor

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"time"
)

// IPApiResponse represents ip-api.com response
type IPApiResponse struct {
	Query   string `json:"query"`
	Country string `json:"country"`
	Status  string `json:"status"`
	Message string `json:"message"`
}

// ProbePoolViaProxy tests the proxy pool itself by making a request through it
// This is useful when direct node probing fails (e.g., due to network restrictions)
func (m *Manager) ProbePoolViaProxy(timeout time.Duration) (bool, string, time.Duration, error) {
	start := time.Now()

	proxyURLStr := "http://lmarch2:LYFnb@@@localhost:2323"
	proxyURL, err := url.Parse(proxyURLStr)
	if err != nil {
		return false, "", 0, fmt.Errorf("parse proxy URL failed: %w", err)
	}

	client := &http.Client{
		Timeout: timeout,
		Transport: &http.Transport{
			Proxy: http.ProxyURL(proxyURL),
		},
	}

	req, err := http.NewRequestWithContext(context.Background(), "GET", "http://ip-api.com/json", nil)
	if err != nil {
		return false, "", 0, fmt.Errorf("create request failed: %w", err)
	}

	// Make request through proxy
	resp, err := client.Do(req)
	if err != nil {
		return false, "", 0, fmt.Errorf("request through proxy failed: %w", err)
	}
	defer resp.Body.Close()

	latency := time.Since(start)

	// Read response
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return false, "", latency, fmt.Errorf("read response failed: %w", err)
	}

	// Parse JSON response
	var result IPApiResponse
	if err := json.Unmarshal(body, &result); err != nil {
		return false, "", latency, fmt.Errorf("parse response failed: %w", err)
	}

	// Check if request was successful
	if result.Status != "success" {
		return false, "", latency, fmt.Errorf("ip-api returned error: %s", result.Message)
	}

	// Success - return the exit IP and country
	location := fmt.Sprintf("%s (%s)", result.Query, result.Country)
	return true, location, latency, nil
}
